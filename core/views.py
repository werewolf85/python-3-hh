from django.shortcuts import render, HttpResponse
from .models import Vacancy
from .models import Company

# Create your views here.
def homepage(request):
    return render(request=request, template_name="index.html")

def about(request):
    return HttpResponse("Найдите работу или работника мечты")

def contact_view(request):
    return HttpResponse('''
    <div>
    Phone: +996777123456 </br>
    Email: office@handhunter.kg
    </div>
    ''')

def address(request):
    return HttpResponse('''
    <div>
        <ol>
            <li>Address: street Chui, 777</li>
            <li>Address: 7 MKR, 20</li>
            <li>Address: 12 MKR, street Nurkamal Jeticashkaeva, 45</li>
        </ol>
    </div>
    ''')

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    context = {"vacancies": vacancies}
    context["example"] = "hello"
    return render(request, 'vacancies.html', context)


def company_list(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    # context["example"] = "hello"

    return render(request, 'companies.html', context)
def vacancy_detail(request, id):
    vacancy_object = Vacancy.objects.get(id=id)  # 1
    candidates = vacancy_object.candidate.all()  # list
    context = {
        'vacancy': vacancy_object,
        'candidates_list': candidates,
    }
    return render(request, 'vacancy/vacancy_page.html', context)


def search(request):
    word = request.GET["keyword"]
    vacancy_list = Vacancy.objects.filter(title__contains=word)
    context = {"vacancies": vacancy_list}
    return render(request, 'vacancies.html', context)
