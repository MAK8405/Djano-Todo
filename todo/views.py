from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

from .forms import TodoForm
from .models import Todo

def index(request):
    item_list = Todo.objects.order_by("-dat")
    if request.method == "POST":
        form.save()
        return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, "todo/index.html", page)

# function to remove item, ire receive todo item_id as primary key from url
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect("todo")




