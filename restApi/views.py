from django.shortcuts import render
from rest_framework import generics

from .models import Todo
from django.http import HttpResponse

from .serializer import TodoSerializer


# Create your views here.

class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoCreate(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoUpdate(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDelete(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRoot(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


