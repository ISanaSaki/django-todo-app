from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo
from .forms import TodoCreateForm, TodoUpdateForm


def home(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
    else:
        todos = Todo.objects.none()
    return render(request, 'home.html', {'todos': todos})


@login_required
def detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    return render(request, 'detail.html', {'todo': todo})


@login_required
def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    messages.success(request, 'object deleted successfully!', 'success')
    return redirect('home')


@login_required
def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, 'ToDo created successfully!', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})


@login_required
def update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'ToDo updated successfully!', 'success')
            return redirect('detail', todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})
