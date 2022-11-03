from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(customer)
class LoginAdmin(admin.ModelAdmin):
    list_display=['Email','password']
    search_fields=['Email','password']