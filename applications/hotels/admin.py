from django.contrib import admin
from applications.hotels.models import Hotels,HotelImage,Comment
# Register your models here.

class ImageAdmin(admin.TabularInline):
    model = HotelImage
    fields = ('image',)
    max_num = 4

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    fields = ('body',)

class HotelsAdmin(admin.ModelAdmin):
    inlines = (ImageAdmin,)
    list_display = ('name','adress',)
    

admin.site.register(Hotels, HotelsAdmin)
admin.site.register(HotelImage)
admin.site.register(Comment)