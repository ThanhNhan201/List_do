from rest_framework import serializers
from .models import ListDo, List

class ListSerializer(serializers.ModelSerializer):
    # todo = ToDoListSerializer()
    class Meta:
        model = List
        fields = (
            'id',
            'list_create_at',
            'list_update_at',
            'list_removed',
            'ping',
            'list_completed',
        )

class ToDoListSerializer(serializers.ModelSerializer):
    # list = ListSerializer()
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
            'list',
        )
        # depth = 1
