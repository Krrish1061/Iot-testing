from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

# from django.core.exceptions import KeyError
from django.contrib.auth import get_user_model
from rest_framework import status
from .utilis import set_data

user_model = get_user_model()


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # content = request.body.decode("utf-8")\
        api_key = request.POST.get("api_key")
        # try:
        #     api_key = set_data(content)["api_key"]
        # except KeyError:
        #     raise AuthenticationFailed(
        #         "Include API key or unsupported format", status.HTTP_401_UNAUTHORIZED
        #     )
        if not api_key:
            raise AuthenticationFailed(
                "Include API key or unsupported format", status.HTTP_401_UNAUTHORIZED
            )
        try:
            user = user_model.objects.get(api_key=api_key)
        except user_model.DoesNotExist:
            raise AuthenticationFailed("Invalid API key", status.HTTP_401_UNAUTHORIZED)
        return (user, None)

    def authenticate_header(self, request):
        return "API-Key"
