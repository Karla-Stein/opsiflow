from django.urls import path
from . import views


urlpatterns = [
    path('my-purchases/', views.purchases,
         name='purchases'),
]