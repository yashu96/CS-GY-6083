from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','created','slug','listing_type','image', 'street_address','city','zipcode','price','description','amenities']

    list_filter = ['created']


admin.site.register(Image, ImageAdmin)
