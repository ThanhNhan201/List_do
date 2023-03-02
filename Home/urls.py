from django.urls import re_path as url
from django.urls import path
from Home import views
from .views import ToDoListApiView, ToDoDetailView


urlpatterns = [
    path('api/<int:id>/', ToDoDetailView.as_view()),
    path('api/', ToDoListApiView.as_view()),
    # url(r'^api/Home/(?P<pk>[0-9]+)$', views.ToDoList_detail),
    # path('api', ToDoListApiView.as_view()),
   
]
