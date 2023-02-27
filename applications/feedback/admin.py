from django.contrib import admin
from applications.feedback.models import Favorite,Rating

# admin.site.register(CommentLike)
admin.site.register(Favorite)
admin.site.register(Rating)