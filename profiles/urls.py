from django.urls import path
from . import views


urlpatterns = [
    path('my-purchases/', views.purchases,
         name='purchases'),
    path('my-profile/', views.my_profile,
         name='my_profile'),
    path('delete-account/', views.delete_account,
         name='delete_account'),
]
