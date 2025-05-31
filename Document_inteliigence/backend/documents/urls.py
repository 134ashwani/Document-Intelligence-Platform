from django.urls import path
from .views import upload_document, list_documents

urlpatterns = [
    path('upload/', upload_document),
    path('documents/', list_documents),
]
