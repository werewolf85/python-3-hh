from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recruiter
from .forms import RecruiterForm


def recruiter_list(request):
    recruiters = Recruiter.objects.all()
    return render(request, 'recruit/list.html', {'recruiters': recruiters})

def create_recruit(request):
    context = {}

    if request.method == "POST":
        recruiter_form = RecruiterForm(request.POST)
        if recruiter_form.is_valid():
            recruiter_form.save()
            return HttpResponse("Готово!")

    recruiter_form = RecruiterForm()
    context["form"] = recruiter_form
    return render(request, 'recruit/recruiter_form.html', context)

def recruit_update(request, id):
    recruit_object = Recruiter.objects.get(id=id)

    if request.method == "POST":
        form = RecruiterForm(data=request.POST, instance=recruit_object)
        if form.is_valid():
            form.save()
            return HttpResponse("Готово!")

    form = RecruiterForm(instance=recruit_object)
    return render(request, "recruit/recruit_edit.html", {"form": form})


def recruiter_detail(request, pk):
    recruiter_object = Recruiter.objects.get(pk=pk)
    return render(
        request,
        'recruit/detail.html',
        {'recruiter_object': recruiter_object}
    )

class RecruitView(View):
    def get(self, request):
        recruiters = Recruiter.objects.all()
        return render(request, 'recruit/list.html', {'recruiters': recruiters})


class RecruitListView(LoginRequiredMixin, ListView):
    model = Recruiter


class RecruiterCreateView(CreateView):
    model = Recruiter
    fields = '__all__'
