from django.contrib import admin
from .models import User

@admin.register(User)
class User_list(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'last_name', 'first_name', 'patronymic')

# Register your models here.
