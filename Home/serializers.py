from rest_framework import serializers
from .models import ListDo, List


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

class ListSerializer(serializers.ModelSerializer):
    todo = ToDoListSerializer(many=True, read_only=True)
    class Meta:
        models = List
        fields = '__all__'