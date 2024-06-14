from django.urls import path
from .views import TodoList, TodoCreate, TodoDetail, TodoUpdate, TodoDelete, TodoListCreate, TodoRoot

urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('/create', TodoCreate.as_view(), name='todo-create'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='todo-update'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='todo-delete'),
    path('todo-list/', TodoListCreate.as_view(), name='todo-list'),
    path('todo-list/<int:pk>/', TodoRoot.as_view(), name='todo-root'),
]