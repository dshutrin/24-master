from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CustomUser)
class AdminUser(admin.ModelAdmin):
	list_display = ('username', 'role')


@admin.register(Role)
class AdminUser(admin.ModelAdmin):
	list_display = ('name', )


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
	list_display = ('name', )


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
	list_display = ('name', )


@admin.register(Product)
class AdminTag(admin.ModelAdmin):
	list_display = ('product_code', 'name', 'price')
	search_fields = ('product_code', )


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
	list_display = ('id', )


@admin.register(ProductTag)
class AdminProductTag(admin.ModelAdmin):
	list_display = ('id', )


@admin.register(UserTrash)
class AdminProductTag(admin.ModelAdmin):
	list_display = ('user', )


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
	list_display = ('id', )
