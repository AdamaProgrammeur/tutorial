from django.contrib import admin
from products.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')  # colonnes visibles
    search_fields = ('nom',)          # barre de recherche

admin.site.register(Product, ProductAdmin)
