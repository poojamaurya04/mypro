from django.urls import path
from myapp import views

urlpatterns = [
    
    path('',views.index),
    path('send',views.send),
    path('showrecord',views.showrecord)
]