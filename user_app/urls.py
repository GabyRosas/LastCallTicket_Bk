from django.urls import path
from .views import RegisterView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from .views import get_user_id

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-id/<str:username>/', get_user_id, name='get_user_id')
]
