from rest_framework import serializers
from .models import ListDo

class ToDoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListDo
        fields = (
            'id',
            'order',
            'color_bg',
            'content',
            'is_completed',
            'created_at',
            'updated_at',
            'removed',
        )