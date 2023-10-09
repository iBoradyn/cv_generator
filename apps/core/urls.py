"""Core urls."""
# Django
from django.contrib.auth.decorators import login_required
from django.urls import path

# Local
from .views import IndexView

app_name = 'core'

urlpatterns = [
    path('', login_required(IndexView.as_view()), name='index'),
]
