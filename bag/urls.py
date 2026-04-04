from django.urls import path
from . import views

urlpatterns = [
     path('', views.view_bag, name='bag'),
     path('add-to-bag/', views.add_to_bag,
          name='add_to_bag'),
     path('remove-from-bag/<int:pk>', views.remove_from_bag,
          name='remove_from_bag'),
     path('change-option/<int:pk>', views.change_option,
          name='change_option')
]
