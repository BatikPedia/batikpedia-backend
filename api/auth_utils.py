from rest_framework_simplejwt.authentication import JWTAuthentication


def get_request_header_authorization(request):
    authorization = request.META.get('HTTP_AUTHORIZATION')
    if not authorization:
        return None

    bearer_token = authorization.split()[1]
    return bearer_token



def user_is_authenticated(request):
    auth_class = JWTAuthentication()
    try:
        bearer_token = get_request_header_authorization(request)
        valid_token = auth_class.get_validated_token(bearer_token)
        get_user = auth_class.get_user(validated_token=valid_token)
        return get_user.is_authenticated
    except:
        return False
    

def get_user_object(request):
    auth_class = JWTAuthentication()
    try:
        bearer_token = get_request_header_authorization(request)
        valid_token = auth_class.get_validated_token(bearer_token)
        get_user = auth_class.get_user(validated_token=valid_token)
        return get_user
    except:
        return None