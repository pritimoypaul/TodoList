from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos', views.todo, name='todos'),
    path('about', views.about, name='about'),
    path('deletetodo/<int:id>', views.deletetodo, name='deletetodo'),
    path('todo_toggle/<int:id>', views.todo_toggle, name='todo_toggle'),
    path('todo/<int:id>', views.todo_single, name='todo'),
    path('todo/<int:id>/edit', views.edit_todo, name='edit_todo'),

]
