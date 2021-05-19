from django.urls import path, re_path

from chat import views

urlpatterns = [
    path('', views.index, name='index_name'),

    path('messages/', views.MessageListView.as_view(), name='messages_name'),
    path('messages/new/created', views.MessageCreateView.as_view(), name='new_message_name'),
    path('messages/new/', views.message_create_render_view, name='new_message_render_name'),
    path('dialogs', views.DialogListView.as_view(), name='dialogs_name'),

    path('register', views.register, name='register_name'),
]
