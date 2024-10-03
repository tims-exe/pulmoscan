from django.urls import path
from . import views

urlpatterns = [
    path('model1/', views.model1),
    path('model2/', views.model2),
    path('testmodel1/', views.testmodel1),
    path('testmodel2/', views.testmodel2),
]

