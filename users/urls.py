from django.urls import path
from .views import *


urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('logout', LogoutView.as_view()),
    path('user', UserView.as_view()),
    path('user/<int:id>', DeleteUserView.as_view()),
]
