from django.contrib import admin
from applications.rooms.models import HotelRooms,RoomImage,Category


class ImageAdmin(admin.TabularInline):
    model = RoomImage
    fields = ('image',)
    max_num = 4

class HotelRoomsAdmin(admin.ModelAdmin):
    inlines = (ImageAdmin,)
    # list_display = ('tltle','category','busy','images')



admin.site.register(HotelRooms,HotelRoomsAdmin)
admin.site.register(RoomImage)
admin.site.register(Category)


