from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserFormView.as_view(), name='home'),
    path('chat/<str:room_name>', views.chat, name='chat')
]