from django.urls import path
from .views import index, CreateEmployee
urlpatterns= [

    path('',index, name="client_index"),
    #path('create/<name>',CreateEmployee, name="client_employee"),
    path('create',CreateEmployee, name="client_employee"),
    
]