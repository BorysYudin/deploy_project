from django.urls import path

from api.views import Hello

urlpatterns = [
    path('hello', Hello.as_view()),
]
