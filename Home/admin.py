from django.contrib import admin
from .models import List, ListDo

@admin.register(ListDo)
class ListDo(admin.ModelAdmin):
    list_display = ('id',
                    'order',
                    'color_bg',
                    'content',
                    'is_completed',
                    'created_at',
                    'updated_at',
                    'removed',
                    'list',
    )


@admin.register(List)
class List(admin.ModelAdmin):
    list_display = (
                    'id',
                    'list_create_at',
                    'list_update_at',
                    'list_removed',
                    'ping',
                    'list_completed',
                    # 'todo'
                    )
# Register your models here.
