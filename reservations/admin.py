from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Reservation admin definition"""

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
    )

    list_filter = ("status",)
