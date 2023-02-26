from django.contrib import admin
from applications.hotels.models import Hotels,HotelImage,Comment
from applications.feedback.models import Rating
from django.db.models import Avg
# Register your models here.    

class RatingAdmin(admin.TabularInline):
    model = Rating 
    fields = ('rating',)
    

class ImageAdmin(admin.TabularInline):
    model = HotelImage
    fields = ('image',)
    max_num = 4

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    fields = ('body',)

class HotelsAdmin(admin.ModelAdmin):
    inlines = (ImageAdmin,RatingAdmin,)
    list_display = ('name','adress','rating_count',)
    
    def rating_count(self, obj):
        return obj.ratings.aggregate(Avg('rating'))['rating__avg']


    

admin.site.register(Hotels, HotelsAdmin)
admin.site.register(HotelImage)
admin.site.register(Comment)