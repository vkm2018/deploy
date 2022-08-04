from django.contrib import admin

# Register your models here.
from applications.product.models import Category, Product, Image, Like, Rating

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Rating)

class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin]
    list_display = ['id', 'name', 'price', 'count_like']

    def count_like(self, obj):
        return obj.likes.filter(like=True).count()


admin.site.register(Product, ProductAdmin)



