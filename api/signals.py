from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
from .utilis import generate_api_key


@receiver(pre_save, sender=settings.AUTH_USER_MODEL)
def handle_user_registered(sender, instance, **kwargs):
    api_key = ""
    while sender.objects.filter(api_key=api_key).exists() or api_key == "":
        api_key = generate_api_key()
    instance.api_key = api_key
