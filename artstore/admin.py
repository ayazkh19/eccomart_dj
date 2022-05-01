from django.contrib import admin
from . models import Category, Product, Customer, Order, OrderItem, ShippingAddress, BannerImage


# admin.py in artstore is used to display all the models in django admin area
# we are inheriting from ModelAdmin to customized the display of our models in admin area.
# right now not a whole lot of customization is needed to the classes are jus there for future use

class BannerImageAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderItemAdmin(admin.ModelAdmin):
    pass


class ShippingAddressAdmin(admin.ModelAdmin):
    pass


# registering our models here
# so django will know to display them
# in order for this to work our 'artstore' should be 'installed'
# which can be seen in ecommarts/settings.py in INSTALLED_APPS list

admin.site.register(BannerImage, BannerImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
