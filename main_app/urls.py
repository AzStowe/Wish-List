from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('items/create/', views.ItemsCreate.as_view(), name='items_create'),
    path('items/<int:pk>/delete/', views.ItemsDelete.as_view(), name='items_delete'),
    path('items/<int:pk>/update/', views.ItemsUpdate.as_view(), name='items_update'),
    path('items/<int:item_id>/', views.items_detail, name='detail'),


]
