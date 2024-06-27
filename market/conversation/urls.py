from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import *
from .models import *
app_name = 'conversations'


urlpatterns=[
    path('new/<int:item_pk>/',views.new_conversation,name='new'),
    path('',views.inbox,name='inbox'),
    path('<int:pk>/',views.detailing,name='detailing'),
]