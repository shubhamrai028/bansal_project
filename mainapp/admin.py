from django.contrib import admin
from mainapp.models import *

# Register your models here.

class schoolcustomization(admin.ModelAdmin):
    list_display = ('Id','Name')
    search_fields = ('Id','Name')
    list_filter = ('Id','Name')
    
admin.site.register(School,schoolcustomization)
    

    
class studentcustomization(admin.ModelAdmin):
    list_display = ('Id','Name','Enrollment')
    search_fields = ('Id','Name','Enrollment')
    list_filter = ('Id','Name','Enrollment')
    
admin.site.register(Student,studentcustomization)