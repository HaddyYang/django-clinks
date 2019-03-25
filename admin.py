from django.contrib import admin
from .models import CustomLink

# Register your models here.
@admin.register(CustomLink)
class CustomLinkAdmin(admin.ModelAdmin):
    list_display = ('text', 'link', 'created_time')
    