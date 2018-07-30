from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Evenet)
admin.site.register(Notification)
admin.site.register(Payment)

admin.site.site_header = 'NSS Administration'