from django.shortcuts import render, redirect
from .models import todos

# Create your views here.


def index(request):
    return render(request, 'todos/index.html',)


def todo(request):
    if request.method == "POST":
        todoname = request.POST.get('todoName')
        description = request.POST.get('description')

        form = todos(todoName=todoname, description=description)

        form.save()
        return redirect('todos')

    todoslist = todos.objects.all().order_by('-id')
    return render(request, 'todos/todos.html', {'todoslist': todoslist})


def about(request):
    return render(request, 'todos/about.html')


def deletetodo(request,id):
    todo_del = todos.objects.get(id=id)
    todo_del.delete()
    return redirect('todos')


def todo_toggle(request,id):
    todo_complete_toggle = todos.objects.get(id=id)
    if todo_complete_toggle.is_complete == False:
        todo_complete_toggle.is_complete = True
    else:
        todo_complete_toggle.is_complete = False

    todo_complete_toggle.save()

    return redirect('todos')


def todo_single(request, id):
    single_todo = todos.objects.get(id=id)
    return render(request, 'todos/single_todo.html', {'single_todo':single_todo})


def edit_todo(request,id):
    if request.method == "POST":
        update_todo = todos.objects.get(id=id)
        updated_name = request.POST.get('todoName')
        updated_description = request.POST.get('description')

        update_todo.todoName = updated_name
        update_todo.description = updated_description
        update_todo.save()

        return redirect('todos')

    todo_for_edit = todos.objects.get(id=id)
    return render(request, 'todos/edit_todo.html', {'todo_for_edit':todo_for_edit})
