from django.urls import path
from .views import ChatbotResponseView, ChatbotIndexView, StartNewSessionView # , UpdateDocumentView


app_name = 'chatbot'
urlpatterns = [
    path('', ChatbotIndexView.as_view(), name='chatbot_index'),
    path("result/", ChatbotResponseView.as_view(), name='chatbot_result'),
    path('new_session/', StartNewSessionView.as_view(), name='new_session'),
    # path("admin/chatbot/update_document/", UpdateDocumentView.as_view(), name='update_document'),
]
