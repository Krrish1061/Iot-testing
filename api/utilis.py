import random
import string
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status


def set_data(content):
    data = {}
    try:
        for params in content.split("&"):
            key, value = params.split("=")
            data[key] = value
    except ValueError:
        raise AuthenticationFailed(
            "Include API key or unsupported format", status.HTTP_401_UNAUTHORIZED
        )
    return data


def generate_api_key():
    """Generate a random API key."""
    api_key_length = 32
    api_key_chars = string.ascii_letters + string.digits
    return "".join(random.choices(api_key_chars, k=api_key_length))
