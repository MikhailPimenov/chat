from django.urls import path, re_path

from chat import views

urlpatterns = [
    path('', views.index, name='index_name'),

    path('messages/', views.MessageListView.as_view(), name='messages_name'),

    path('messages/new/created', views.MessageCreateView.as_view(), name='new_message_name'),

    path('messages/new/', views.MessageCreateFormView.as_view(), name='new_message_render_name'),

    path('dialogs', views.DialogListView.as_view(), name='dialogs_name'),

    # path('dialogs/new/', views.DialogSearchResultView.as_view(), name='dialogs_search_result_name'),
    # path('dialogs/new/', views.DialogSearchDetailView.as_view(), name='dialogs_search_result_name'),
    path('dialogs/search/', views.dialog_search_or_create_view, name='dialogs_search_result_name'),

    path('dialogs/new/', views.DialogCreateView, name='new_dialog_name'),

    path('users/search', views.UserSearchFormView.as_view(), name='users_search_name'),

    path('users/search/results', views.UserSearchResultView.as_view(), name='users_search_results_name'),

    path('blacklist', views.BlacklistDetailView.as_view(), name='blacklist_name'),

    path('blacklist/update', views.update_blacklist, name='blacklist_update_name'),

    path('register', views.register, name='register_name'),
]
