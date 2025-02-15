from django.contrib import admin
from .models import Moviedata , Movies
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name","duration","rating")

# Register your models here.

admin.site.register(Moviedata,MovieAdmin)
admin.site.register(Movies)