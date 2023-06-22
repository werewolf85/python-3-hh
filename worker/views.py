from django.shortcuts import render, HttpResponse
from .models import Worker
# Create your views here.
def worker_list(request):
    workers = Worker.objects.all()
    context = {"workers": workers}
    # context["example"] = "hello"

    return render(request, 'workers.html', context)