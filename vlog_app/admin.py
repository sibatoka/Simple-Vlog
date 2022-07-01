from django.contrib import admin
from .models import Post, Contact, SiteInfo

# Register your models here.

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(SiteInfo)
