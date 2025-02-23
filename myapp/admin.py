from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *

# Register your models here.

admin.site.register(Mobile)
admin.site.register(Customer)
admin.site.register(Monitor)
admin.site.register(Earphone)
admin.site.register(GamingConsole)
admin.site.register(Games)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(OrderPlaced)
