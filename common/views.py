from django.shortcuts import render

from django.views.generic import ListView

from .models import SavedRequest


class RequestListView(ListView):
    queryset = SavedRequest.objects.all()[:10]
    context_object_name = "request_list"
    template_name = 'request_list.html'
