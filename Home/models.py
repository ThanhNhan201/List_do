from django.db import models

# Create your models here.

class List(models.Model):
    list_create_at = models.DateTimeField(auto_now_add=True)
    list_update_at = models.DateTimeField(auto_now=True)
    list_removed = models.BooleanField(default=False)
    ping = models.BooleanField(default=False)
    list_completed = models.BooleanField(default=False)

class ListDo(models.Model):
    order = models.IntegerField(default=0)
    color_bg = models.CharField(default="fff",blank=True, max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE,blank=True,null=True)


    class Meta:
        ordering = ["order"]

    # def __str__(self):
    #     return self.order


