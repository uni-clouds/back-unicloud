from rest_framework.viewsets import ModelViewSet
from unicloud_users.api.serializers import UserListSerializer, LoginTokenSerializer, MenuSerializer, UserSerializer, InvitedUserListSerializer, InvitedUserSerializer, InvalidTokenSerializer
from unicloud_users.models import UserProfile
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from ..menu import customer_menu, admin_menu
from rest_framework.renderers import JSONRenderer
from unicloud_customers.models import UserCustomer, InvitedUser, Customer
from django.shortcuts import get_object_or_404
from error_messages import messages
from check_root.unicloud_check_root import CheckRoot
from unicloud_tokengenerator.generator import TokenGenerator
from django.template.loader import get_template
from unicloud_mailersystem.mailer import UniCloudMailer
from logs.setup_log import logger

class UsersViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    def retrieve(self, request):
        checkroot = CheckRoot(request)
        if checkroot.is_root():
            userlist = User.objects.filter(is_staff=True, is_superuser=True)
            serializer = UserListSerializer(userlist, many=True)
            return Response(serializer.data)
        customer_id = UserCustomer.objects.get(user_id=request.user.id).customer_id
        userlist_bycustomer = UserCustomer.objects.filter(customer_id=customer_id)
        ids = []
        for item in userlist_bycustomer:
            ids.append(item.user_id)
        userlist = User.objects.filter(id__in=ids)
        serializer = UserListSerializer(userlist, many=True)
        return Response(serializer.data)

    def create(self, request):
        customer_id = UserCustomer.objects.get(user_id=request.user.id).customer_id
        customer = Customer.objects.get(id=customer_id)
        try:
            token_generator = TokenGenerator(request.data['email'])
            token = token_generator.gettoken()
            invited_user, created = InvitedUser.objects.get_or_create(email=request.data['email'],token=token, customer=customer)
            if created:
                try:
                    mensagem = {
                        'empresa': customer.razao_social,
                        'link': f'http://127.0.0.1:3000/auth-register/?token={token}'
                    }
                    rendered_email = get_template('email/welcome.html').render(mensagem)
                    mailer = UniCloudMailer(request.data['email'], 'Bem vindo ao Uni.Cloud Broker', rendered_email)
                    mailer.send_mail()
                except Exception as error:
                    print(error)
                    return Response(messages.email_notsent, 400)
        except Exception as error:
            print(error)
            return Response(messages.bad_request, 400)

        return Response({'status':'created'})

class RegisterViewSet(viewsets.ViewSet):
    def create(self, request):
        isRoot = False
        if request.user.is_superuser and request.user.is_staff:
            isRoot = True
        is_invited = get_object_or_404(InvitedUser, email=request.data['username'])
        serialized_data = None
        try:
            user = User.objects.create_user(username=request.data['username'], password=request.data['password'], email=request.data['username'], first_name=request.data['first_name'], last_name=request.data['last_name'], is_staff=isRoot, is_superuser=isRoot)

            userprofile = UserProfile(phone=request.data['phone'], address=request.data['address'], city=request.data['city'], state=request.data['state'], country=request.data['country'], user=user)
            userprofile.save()

            customer = Customer.objects.get(id=is_invited.customer.id)
            customer = UserCustomer(user=user, customer=customer)
            customer.save()

            serialized_data = UserSerializer(user)
        except Exception as error:
            return Response(messages.permission_denied, 404)
        finally:
            is_invited.delete()
            return Response(serialized_data.data)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginTokenSerializer
    def get_object(self):

        return self.request.user

class MenuViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def retrieve(self, request):
        if request.user.is_superuser and request.user.is_staff:
            menu = [*admin_menu, *customer_menu]
            return Response(JSONRenderer().render(menu))
        serializer = MenuSerializer(customer_menu)
        return Response(JSONRenderer().render(customer_menu))

class InvitedUsersViewSet(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated)
    def create(self, request):
        customer = Customer.objects.get(id=1)
        inviteduser = InvitedUser(token=request.data['token'], email=request.data['email'], customer=customer)
        inviteduser.save()
        serializer = InvitedUserSerializer({'teste': 'teste'})
        return Response(JSONRenderer().render(serializer.data))

    def retrieve(self, request):
        organization = UserCustomer.objects.get(user_id=request.user.id)
        print(organization.customer_id)
        invited_users_list = InvitedUser.objects.filter(customer_id=organization.customer_id)
        print(invited_users_list)
        serializar = InvitedUserListSerializer(invited_users_list, many=True)

        return Response(serializar.data)

class TokenViewSet(viewsets.ViewSet):

    def check_token(self, request):
        token = InvitedUser.objects.filter(token=request.data['token']).exists()
        if token:
            token_data = InvitedUser.objects.get(token=request.data['token'])
            serializer = InvitedUserSerializer({'id':token_data.id, 'token':token_data.token, 'email':token_data.email, 'razao_social':token_data.customer.razao_social, 'is_valid':True})
            return Response(serializer.data)

        serializer = InvalidTokenSerializer({'is_valid':False})
        return Response(serializer.data)