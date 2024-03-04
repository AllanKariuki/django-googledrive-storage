from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .models import File
from .serializers import FileSerializer

class Files(viewsets.ViewSet):
    def list(self, request):
        try:
            files = File.objects.all()
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    def create(selfself, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        file = File.objects.get(id=pk)
        serializer = FileSerializer(file)
        return Response(serializer.data)

    def update(self, request, pk=None):
        file = File.objects.get(id=pk)
        serializer = FileSerializer(instance=file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk = None):
        File.objects.get(id=pk).delete()
        return Response(status = status.HTTP_200_OK)