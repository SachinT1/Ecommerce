from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'item'
urlpatterns=[
    path('<int:pk>/',views.detail,name='detail'),
    path('new/',views.new,name='new'),
    path('browse/',views.browse,name='browse'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/edit/',views.edit,name='edit'),
    path('newcat/',views.newcat,name='newcat'),
]
