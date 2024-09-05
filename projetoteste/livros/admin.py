from django.contrib import admin
from .models import livro
# Register your models here.

class LivrosAdmin(admin.ModelAdmin):
    list_display = ["titulo"]

admin.site.register(livro, LivrosAdmin)
