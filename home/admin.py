from django.contrib import admin
from home.models import Order, Update

# Register your models here.
admin.site.register((Order, Update))
