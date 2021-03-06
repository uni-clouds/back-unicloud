from django.conf import settings
import requests
from logs.setup_log import logger
import os

class UniCloudMailer:
    def __init__(self, recipient, subject, email):
        self.url = "https://api.mailgun.net/v3/uni.cloud/messages"
        self.auth = ("api", settings.APIKEY_MAILGUN)
        self.data = {
            "from": settings.EMAIL_FROM,
            "to": recipient,
            "subject": subject,
            "text": "Permita a leitura de email via HTML, ou contacte nosso suporte",
            "html": email
        }

    def send_mail(self):
        try:
            sendmail = requests.post(
                self.url,
                auth=self.auth,
                data=self.data
            )
            logger.info(sendmail.json())
        except Exception as error:
            logger.error(error)