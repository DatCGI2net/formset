from django.contrib import admin

# Register your models here.

from setup.models import Setup, Specification

class SetupAdmin(admin.ModelAdmin):
    
    pass

admin.site.register(Setup, SetupAdmin)

class SpecificationAdmin(admin.ModelAdmin):
    
    pass

admin.site.register(Specification, SpecificationAdmin)
