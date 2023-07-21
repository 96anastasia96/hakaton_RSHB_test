from django.urls import path
from .views import register_user, login_view, LogoutViewCustom

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutViewCustom, name='logout'),
    path('signup/', register_user, name='signup'),
]