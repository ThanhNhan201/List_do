from rest_framework import serializers
from .models import ListDo, List


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class ToDoListSerializer(serializers.ModelSerializer):
    list = ListSerializer()
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

