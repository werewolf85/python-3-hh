from django.shortcuts import render, HttpResponse
from .models import Worker
# Create your views here.
def worker_list(request):
    workers = Worker.objects.all()
    context = {"workers": workers}
    # context["example"] = "hello"

    return render(request, 'workers.html', context)

def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    vacancies = worker_object.vacancy_set.all
    context = {
        "worker": worker_object,
        "vacancies": vacancies,
    }
    return render(request, 'worker.html', context)