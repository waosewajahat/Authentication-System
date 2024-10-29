from django.urls import path
from .views import register, user_login, home, user_logout  # Import the user_logout view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),  # Add this line for logout
    path('', home, name='home'),  # Home view
]
