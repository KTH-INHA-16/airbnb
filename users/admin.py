from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

"""decorator"""


@admin.register(models.User)
class UserAdmin(UserAdmin):

    """ Custom User Admin """

    """list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = (
        "language",
        "currency",
        "superhost",
    )"""
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avator",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
