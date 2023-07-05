from django.shortcuts import render, HttpResponse, redirect
from .models import Vacancy
from .models import Company
from django.contrib.auth.models import User
from .forms import VacancyForm

# Create your views here.
def homepage(request):
    return render(request=request, template_name="index.html")


def vacancy_add_via_django_form(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            new_vacancy = form.save()
            return redirect(f'/vacancy/{new_vacancy.id}/')
    vacancy_form = VacancyForm()
    return render(
        request,
        'vacancy/vacancy_django_form.html',
        {"vacancy_form": vacancy_form}
    )

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
    # context["example"] = "hello"
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
def reg_view(request):
    if request == "POST":
        user = User(
            username=request.POST["username"]
        )
        user.save()
        user.set_password(request.POST["password"])
        user.save()
        return HttpResponse('Готово!')

    return render(
        request,
        "auth/registr.html"
    )

def vacancy_add(request):
    if request.method == "POST":
        new_vacancy = Vacancy(
            title=request.POST["title"],
            salary=int(request.POST["salary"]),
            description=request.POST["description"],
            email=request.POST["email"],
            contacts=request.POST["contacts"],
        )
        new_vacancy.save()
        return redirect(f'/vacancy/{new_vacancy.id}/')
    return render(request, 'vacancy/vacancy_form.html')


def vacancy_edit(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if request.method == "POST":
        vacancy.title = request.POST["title"]
        vacancy.salary = int(request.POST["salary"])
        vacancy.description = request.POST["description"]
        vacancy.email = request.POST["email"]
        vacancy.contacts = request.POST["contacts"]
        vacancy.save()
        return redirect(f'/vacancy/{vacancy.id}/')
    return render(
        request, 'vacancy/vacancy_edit_form.html',
        {"vacancy": vacancy}
    )
