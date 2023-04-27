from django.urls import path
from .views import *

urlpatterns = [
    path('get_data/', GetUserData.as_view() ),
    path('create_data/',CreateUserData.as_view()),
    path('update_data/<int:pk>', EditUserData.as_view()),
    path('delete_data/<int:pk>',DeleteUserData.as_view())
]