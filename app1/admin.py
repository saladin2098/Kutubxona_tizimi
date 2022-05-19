from django.contrib import admin
from django.contrib.admin import  ModelAdmin
from .models import *
#admin.site.register(kitob)
admin.site.register(record)
# admin.site.register(Student)

@admin.register(Muallif)
class MuallifAdmin(ModelAdmin):

    list_display = ("id","ism","yosh" ,"tirik",)
    list_display_links = ("ism","yosh","tirik",)

    list_filter = ("tirik",)
    search_fields = ("ism" , "id",)


@admin.register(Student)
class StudentAdmin(ModelAdmin):
    search_fields = ("ism" , "id", "guruh",)
    list_editable = ("kitob_soni",)
    list_filter = ("guruh",)
    list_display = ("id","ism","guruh","kitob_soni")
    list_display_links = ("id","ism","guruh",)

@admin.register(kitob)
class kitobAdmin(ModelAdmin):
    search_fields = ("nomi","id",)
    list_display = ("id","nomi","sahifa","janr",)
    list_display_links = ("nomi",)
    list_editable = ("sahifa","janr",)
    list_filter = ("janr",)
    autocomplete_fields = ("muallif",)

