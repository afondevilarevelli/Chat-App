from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserLoginView.as_view(), name='login'),
    path('sign-up', views.UserCreateView.as_view(), name='sign-up'),
    path('chats', views.chat, name='chats')
]