from django.contrib import admin
from .models import Articles


# Регистрируем нашу базу данных в админке

admin.site.register(Articles)
