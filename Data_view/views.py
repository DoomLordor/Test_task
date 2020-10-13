from django.shortcuts import render
from django.views.generic.base import View

from .models import Data

class DataView(View):
    """Просмотр сводных данных"""
    def get(self, request):
        data = Data.objects.all()
        return render(request, 'index.html', {'data_list': data})
