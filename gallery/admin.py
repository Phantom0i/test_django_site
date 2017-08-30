from django.contrib import admin

# Register your models here.
from gallery.models import ImgModel


@admin.register(ImgModel)
class ImgAdmin(admin.ModelAdmin):
    list_display = ('img', )

