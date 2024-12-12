from django.contrib import admin

from actors.models import Actor


# Register your models here.
@admin.register(Actor)
class AdminActor(admin.ModelAdmin):
    list_display = ("id", "name", "birthday", "nationality")
