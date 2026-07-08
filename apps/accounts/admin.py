from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "temp_unit",
        "is_staff",
    )

    search_fields = (
        "username",
        "email",
    )

    list_filter = (
        "temp_unit",
        "is_staff",
        "is_superuser",
    )