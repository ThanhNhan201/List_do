from django.shortcuts import render

# from django.http.response import JsonResponse
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework import permissions

from Home.models import ListDo
from Home.serializers import ToDoListSerializer
# from rest_framework.decorators import api_view

# class ToDoListApiView(APIView):
#     def get(self, request): 
#         if request.method == 'GET':
#             todo = ListDo.objects.filter(removed = False)
#             serializer = ToDoListSerializer(todo, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request):
#         if request.method == 'POST':
#             order  = request.data.get('order')
#             color_bg  = request.data.get('color_bg')
#             content = request.data.get('content')
#             is_completed  = request.data.get('is_completed')
#             removed  = request.data.get('removed')
#             todo = ListDo.objects.create(
#                     order = order,
#                     color_bg=color_bg,
#                     content=content,
#                     is_completed=is_completed,
#                     removed=removed
#                 )
#             return Response({
#                 'ok': True,
#                 'data': ToDoListSerializer(todo).data,
#                 'msg': 'Tao thanh cong.'
#             },
#             status=201)
        
# class ToDoDetailView(APIView):
#     def get_object(self, id):
#         try:
#             return ListDo.objects.get(id = id)
#         except ListDo.DoesNotExist:
#             return None
        
#     def get(self, request, id,  format=None):
#             todo_instance = self.get_object(id)
#             if not todo_instance:
#                 return Response(
#                     {"res": "Object with todo id does not exists"},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )
#             serializer = ToDoListSerializer(todo_instance)
#             return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put (self, request, id,  format=None):
#         if request.method == 'PUT':
#             todo_instance = self.get_object(id)
#             if not todo_instance:
#                 return Response(
#                     {"res": "Object with todo id does not exists"},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )
#             serializer = ToDoListSerializer(todo_instance, data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=200)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, id,  format=None):
#             if request.method == 'DELETE':
#                 todo_instance = self.get_object(id)
#                 todo_instance.delete()
#                 return Response(status=status.HTTP_204_NO_CONTENT)
        





class ToDoListApiView(APIView):
    def get (self, request):
        obj = ListDo.objects.filter(removed=False)
        color_bg  = request.data.get('color_bg')
        # if len(color_bg) > 6:
        #     return Response({'msg':'Ma mau phai co gia tri la 3 chu so hoac 6 chu so'})
        serializer = ToDoListSerializer(obj, many = True)
        return Response(serializer.data, status = 200)
    
    def post (self, reqtuest):
        serializer = ToDoListSerializer(data = reqtuest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ToDoDetailView(APIView):
    def get (self, request, id):
        try:
            obj = ListDo.objects.get(id=id)
        except ListDo.DoesNotExist:
            msg = {"msg": "not found"}
            return  Response(msg, status=status.HTTP_400_BAD_REQUEST)
        serializer = ToDoListSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put (self, request, id):
        try:
            obj = ListDo.objects.get(id=id)
        except ListDo.DoesNotExist:
            msg = {"msg": "not found"}
            return  Response(msg, status=status.HTTP_400_BAD_REQUEST)

        serializer = ToDoListSerializer(obj, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete (self, request, id):
        try:
            obj = ListDo.objects.get(id=id)
        except ListDo.DoesNotExist:
            msg = {"msg": "not found"}
            return  Response(msg, status=status.HTTP_400_BAD_REQUEST)

        obj.delete()
        return Response({'msg': 'deleted'}, status = status.HTTP_204_NO_CONTENT)