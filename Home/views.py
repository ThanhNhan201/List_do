from django.shortcuts import render

# from django.http.response import JsonResponse
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from rest_framework import status, generics, viewsets
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
        # obj = ListDo.objects.all()
        obj = ListDo.objects.filter(removed=False)
        # color_bg = request.data.get('color_bg')

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

class finish(generics.UpdateAPIView):
    serializer_class = ToDoListSerializer
    model = ListDo
    # permission_classes = (IsAuthenticated,)
    def put(self, request, id, *args, **kwargs):
        try:
            queryset = ListDo.objects.get(id=id)
        except ListDo.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        # queryset = self.filter_queryset(self.get_queryset())
        # queryset = ListDo.objects.get(id=id)
        queryset.is_completed = True
        serializer = serializers(queryset)
        # print(queryset)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# def finish(request, id):
#     try:
#         obj = ListDo.objects.get(id=id)
#     except ListDo.DoesNotExist:
#         msg = {"msg": "not found"}
#         return Response(msg, status=status.HTTP_400_BAD_REQUEST)
#     obj.is_completed = True
#     serializer = ToDoListSerializer(data=obj)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateOrder(generics.ListCreateAPIView):
    queryset = ListDo.objects.all()
    serializer_class = ToDoListSerializer

    def put(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        instances = list(queryset)
        count = len(instances)
        # data = {}
        # for i in range(count):
        #     data = dict(list(data.items()) + list(request.data.items()))
        data = [request.data] * count
        # import array as arr
        # a = arr.array('d', [data])
        print(data)
        serializer = ToDoListSerializer(instances, data, many=True, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_list_update(serializer)
        return Response(status=204)

    def perform_list_update(self, serializer):
        # for
        for instance, data in zip(serializer.instance, serializer.validated_data):
            for attr, value in data.items():
                setattr(instance, attr, value)
            instance.save()



