
permission_denied = {
    'data': {
        'detail': 'User not allowed to perform this operation.',
        'code': 'not_allowed',
        'messages': [
            {
                'token_class': 'AccessToken',
                'token_type': 'access',
                'message': 'User not allowed to perform this operation.',
            }
         ]
    }
}

already_exist = {
    'data': {
        'detail': 'Register already exists',
        'code': 'not_allowed',
        'messages': [
            {
                'token_class': 'AccessToken',
                'token_type': 'access',
                'message': 'You try to save some register who already exist',
            }
         ]
    }
}

email_notsent = {
    'data': {
        'detail': 'Error in mailer system',
        'code': 'email_notsent',
        'messages': [
            {
                'token_class': 'AccessToken',
                'token_type': 'access',
                'message': 'We can`t sent the e-mail',
            }
        ]
    }
}

bad_request = {
    'data': {
        'detail': 'bad request',
        'code': 'exception_occured',
        'messages': [
            {
                'token_class': 'AccessToken',
                'token_type': 'access',
                'message': 'An exception occured',
            }
        ]
    }
}