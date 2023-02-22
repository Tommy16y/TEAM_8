from django.contrib import admin
from applications.rooms.models import HotelRooms,RoomImage,Category,Price


class ImageAdmin(admin.TabularInline):
    model = RoomImage
    fields = ('image',)
    max_num = 4

class PriceAdmin(admin.TabularInline):
    model = Price
    fields = ('price','category',)
    max_num =1


class HotelRoomsAdmin(admin.ModelAdmin):
    inlines = (ImageAdmin,PriceAdmin)
    # list_display = ('tltle','category','busy','images')


admin.site.register(HotelRooms,HotelRoomsAdmin)
admin.site.register(RoomImage)
admin.site.register(Category)
admin.site.register(Price)

