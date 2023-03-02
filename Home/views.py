from django.shortcuts import render

# from django.http.response import JsonResponse
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework import permissions
from rest_framework import serializers
from .models import ListDo
from .serializers import ToDoListSerializer


# def update(self, request):
#     obj = ListDo.objects.all()
#     ListDo.objects.bulk_update(obj, ['order'])


class ToDoListApiView(APIView):
    def get(self, request):
        obj = ListDo.objects.filter(removed=False)
        color_bg = request.data.get('color_bg')

        serializer = ToDoListSerializer(obj, many=True)
        return Response(serializer.data, status=200)

    def post(self, reqtuest):
        serializer = ToDoListSerializer(data=reqtuest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        todo = ListDo.objects.all()
        for obj in todo:
            obj.delete()
        return Response({'msg': 'all deleted'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        obj = ListDo.objects.get()
        # qs = obj.objects.filter(removed=False).order_by('order')
        for i in list(obj):
            order = request.data.get('order')
            content = request.data.get('content')
            color_bg = request.data.get('color_bg')
            is_completed = request.data.get('is_completed')
            ls_todo = [{'order': order, 'content': content, 'color_bg': color_bg, 'is_completed': is_completed}]
        qs = ls_todo.objects.filter(removed=False).order_by('order')
        serializer = ToDoListSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoDetailView(APIView):
    def get (self, request, id):
        try:
            obj = ListDo.objects.get(id=id)
        except ListDo.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        serializer = ToDoListSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


    
    def put (self, request, id):
        try:
            obj = ListDo.objects.get(id=id)
        except ListDo.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

        serializer = ToDoListSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete (self, request, id):
        try:
            obj = ListDo.objects.get(id=id)
        except ListDo.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

        obj.delete()
        return Response({'msg': 'deleted'}, status=status.HTTP_204_NO_CONTENT)

# class finish(APIView):
#     def finish(self, request, id):
#         obj = ListDo.objects.get(id=id)
#         obj.is_completed = serializers.BooleanField(default=True)
#         # serializer = ToDoListSerializer(obj)
#         if obj.is_completed.is_valid():
#             obj.is_completed.save()
#             return Response(obj, status=status.HTTP_205_RESET_CONTENT)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#


# class UpdateOder(APIView):
#     def put(self, request):
#         obj = ListDo.objects.get()
#         # qs = obj.objects.filter(removed=False).order_by('order')
#         for i in list(obj):
#             order = request.data.get('order')
#             content = request.data.get('content')
#             color_bg = request.data.get('color_bg')
#             is_completed = request.data.get('is_completed')
#             ls_todo = [{'order': order, 'content': content, 'color_bg': color_bg, 'is_completed': is_completed}]
#         qs = ls_todo.objects.filter(removed=False).order_by('order')
#         serializer = ToDoListSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





