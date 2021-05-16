from django.urls import path

from chat import views

urlpatterns = [
    path('', views.index, name='index'),
    path('messages', views.MessageListView.as_view()),
    path('dialogs', views.DialogListView.as_view()),
    path('register', views.register, name='register'),
]
