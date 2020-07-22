from django.contrib import admin
from . import models


@admin.register(models.List)
class RegisterAdmin(admin.ModelAdmin):

    pass
