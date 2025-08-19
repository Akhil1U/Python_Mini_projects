from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    # path('add', views.addTodo, name='add'),
    # path('complete/<todo_id>', views.completeTodo, name='complete'),
    # path('deleteall', views.deleteAll, name='deleteall'),
]