from django.urls import path
from . import views

urlpatterns = [
    path('model1/', views.model1),
    path('model2/', views.model2),
]

