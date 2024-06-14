from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from . import models

# Create your views here.

def todo_list(request):
    all_data = {'todo_list':models.Todoapp.objects.all()}
    return render(request,'to_do_app/todo_list.html',all_data)


def insert_todo(request:HttpRequest):
    todo = models.Todoapp(task_description = request.POST['content'])
    todo.save()
    return redirect('/todo/list')
    
def delete_todo_item(request,todo_id):
    delete_id = models.Todoapp.objects.get(id = todo_id)
    delete_id.delete()
    return redirect('/todo/list')