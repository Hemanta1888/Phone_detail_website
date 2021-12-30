from django.contrib import admin
from .models import *

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['Pname','Porigin','Pyear','Pabout']
    list_display_links = ['Porigin']


class modelDetailAdmin(admin.ModelAdmin):
    list_display = ['mname','mprice','phonemodel','mabout']
    list_display_links = ['mname']


admin.site.register(PhoneModel,PhoneAdmin)
admin.site.register(ModelDetail,modelDetailAdmin)