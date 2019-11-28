from django.contrib import admin
from CBVApp.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','pname','price','description']
# Register your models here.
admin.site.register(Product,ProductAdmin)
