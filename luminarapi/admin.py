from django.contrib import admin
from .models import User,DemoClass,Details,VideoScreenClass,Logo,LiveClass,Module

# admin.site.register(Courses)

admin.site.register(DemoClass)
admin.site.register(Details)
admin.site.register(Module)
# admin.site.register(Modules)
admin.site.register(VideoScreenClass)
admin.site.register(Logo)
admin.site.register(LiveClass)



# Register your models here.
