from django.contrib import admin
from .models import movie
# Register your models here.
class movieadmin(admin.ModelAdmin):
    list = ['name','pic','url1','url2','url3','url4','url5','url6','url7','url8','url9''url10']
    
admin.site.register(movie,movieadmin)