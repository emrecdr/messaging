from django.urls import path
from .views import MessageListApiView

urlpatterns = [
    path('messages/', MessageListApiView.as_view()),
]