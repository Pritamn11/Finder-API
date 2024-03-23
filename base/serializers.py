from rest_framework import serializers
from .models import EventManage


class EventManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventManage
        fields = '__all__'