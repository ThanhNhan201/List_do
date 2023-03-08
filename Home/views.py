from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics,viewsets
from rest_framework.views import APIView
from rest_framework import serializers
from .models import ListDo, List
from .serializers import ToDoListSerializer, ListSerializer
    # ListSerializer

class ToDoListApiView(generics.ListCreateAPIView):
    queryset = ListDo.objects.filter(removed=False)
    serializer_class = ToDoListSerializer
    def get(self, request):
        # obj = ListDo.objects.all()
        obj = ListDo.objects.filter(removed=False)
        serializer = ToDoListSerializer(obj, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):

        serializer = ToDoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        todo = ListDo.objects.all()
        for obj in todo:
            # obj.delete()
            obj.removed = True
            serializer = ToDoListSerializer(data=obj)
            if serializer.is_valid():
                serializer.save()
            obj.save()
        return Response({'msg': 'all deleted'}, status=status.HTTP_204_NO_CONTENT)

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
        # obj.delete()
        obj.removed = True
        serializer = ToDoListSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()
        obj.save()
        return Response({'msg': 'deleted'}, status=status.HTTP_204_NO_CONTENT)

# class finish(generics.UpdateAPIView):
#     serializer_class = ToDoListSerializer
#     model = ListDo
#     def put(self, request, id, *args, **kwargs):
#         try:
#             queryset = ListDo.objects.get(id=id)
#         except ListDo.DoesNotExist:
#             msg = {"msg": "not found"}
#             return Response(msg, status=status.HTTP_400_BAD_REQUEST)
#         # queryset = self.filter_queryset(self.get_queryset())
#         # queryset = ListDo.objects.get(id=id)
#         queryset.is_completed = True
#         serializer = serializers(queryset)
#         # print(queryset)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class finish(generics.UpdateAPIView):
#     queryset = ListDo.objects.filter(removed=False)
#     serializer_class = ToDoListSerializer
#     lookup_field = 'id'
#     print('cc')
#     def finish(self, request, id):
#         print('huhu')
#         # queryset = ListDo.objects.filter(id=id).update(is_completed=True)
#         queryset = ListDo.objects.filter(id=id)
#         queryset.is_completed = True
#         serializer = serializers(queryset)
#         # print(serializer)
#         if serializer.is_valid():
#             serializer.save()

class UpdateOrder(generics.ListCreateAPIView):
    def get(self, request):
        obj = ListDo.objects.filter(removed=False)
        serializer = ToDoListSerializer(obj, many=True)
        return Response(serializer.data, status=200)
    queryset = ListDo.objects.all()
    # queryset = ListDo.objects.filter(removed=False)
    serializer_class = ToDoListSerializer
    def put(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        instances = list(queryset)
        print(instances)
        count = len(instances)
        # data = []
        # for i in range(count):
        #     x = data.request
        #     data = np.concatenate((data, x), axis=0)
        data = [request.data] * count
        # import array as arr
        # a = arr.array('d', [data])
        print(data)
        serializer = ToDoListSerializer(instances, data, many=True, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_list_update(serializer)
        return Response(status=204)

    def perform_list_update(self, serializer):
        for instance, data in zip(serializer.instance, serializer.validated_data):
            for attr, value in data.items():
                setattr(instance, attr, value)
            instance.save()

###################
class ListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        obj = List.objects.all()
        serializer = ListSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)