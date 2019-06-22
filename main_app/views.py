from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Item

# Create your views here.

def home(request):
    item_list = Item.objects.all()
    print(f'{item_list}')
    return render(request, 'home.html', {'item_list':item_list})


class ItemsCreate(CreateView):
    model = Item
    fields = '__all__'

class ItemsDelete(DeleteView):
    model = Item
    success_url = '/'

class ItemsUpdate(UpdateView):
    model = Item
    fields = '__all__'

def items_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'items/detail.html', { 'item': item })