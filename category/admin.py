from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}  # Usa un diccionario con tupla para los campos prepopulados
    list_display = ('category_name', 'slug')  # Usa una tupla o lista para los campos que se mostrarán en la lista

admin.site.register(Category, CategoryAdmin)
