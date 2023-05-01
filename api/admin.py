from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, MachineDescription, SensorValue


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "first_name", "api_key")
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )


# Register your models here.


@admin.register(MachineDescription)
class MachineDescriptionAdmin(admin.ModelAdmin):
    list_display = ("machine_id", "machine_location", "user", "is_active")


@admin.register(SensorValue)
class SensorValueAdmin(admin.ModelAdmin):
    list_display = ("machine_id", "temperature", "humidity", "mains")
