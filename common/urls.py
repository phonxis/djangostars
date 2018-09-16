from django.urls import path

from .views import (
    RequestListView
)


app_name = 'common'  # need for include function in root urls.py

urlpatterns = [
    path('', RequestListView.as_view(), name='request-list'),
]
