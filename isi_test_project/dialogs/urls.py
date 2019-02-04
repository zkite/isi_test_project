from django.urls import path
from dialogs.views import (
    CreateThreadView,
    CreateMessageView,
    GetMessageListView,
    GetThreadListView,
    UpdateThreadView,
)


urlpatterns = [
    path('thread/create', CreateThreadView.as_view(), name='threads'),
    path('thread/list', GetThreadListView.as_view(), name='threads-list'),
    path('thread/update/<int:pk>', UpdateThreadView.as_view(), name='threads-update'),
    path('message/create', CreateMessageView.as_view(), name='message-create'),
    path('message/list/<int:thread>', GetMessageListView.as_view(), name='message-list')
]