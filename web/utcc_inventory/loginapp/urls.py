from django.urls import path
from loginapp import views

urlpatterns = [
    path('',views.index ),
    path('about',views.about),
    path('form',views.form)
]