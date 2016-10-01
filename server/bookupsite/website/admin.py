from django.contrib import admin
from .models import *


#This allows for the admin to create and manage objects in the database
#This will not work when debug = false
admin.site.register(UserBuddy)
admin.site.register(Class)
admin.site.register(Groups)
admin.site.register(StudyBuddy)
admin.site.register(Message)

