from django.contrib import admin
from .models import Profile, Songs, Traditonsongs, LatestContact, Post

admin.site.register(Profile)
admin.site.register(Songs)
admin.site.register(Traditonsongs)
admin.site.register(LatestContact)
admin.site.register(Post)

