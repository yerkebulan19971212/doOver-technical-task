from django.urls import path
from .views import CategoriesListView, SendToEmailView


app_name = "extra"
urlpatterns = [
    path("categories/", CategoriesListView.as_view(), name='categories'),
    path("send-to-email/", SendToEmailView.as_view())
]
