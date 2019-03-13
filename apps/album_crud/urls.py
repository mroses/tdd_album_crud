from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dash', views.dashboard),
    path('album/<album_id>', views.single_album),
    path('album/<album_id>/edit', views.edit),
    path('create', views.create),
    path('<album_id>/delete', views.delete),
    path('<album_id>/read', views.read)
]
