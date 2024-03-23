from django.contrib import admin
from .models import EventManage
# Register your models here.


class EventManageAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_name', 'city_name', 'date', 'time', 'latitude', 'longitude')


admin.site.register(EventManage, EventManageAdmin)