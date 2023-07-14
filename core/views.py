from django.shortcuts import render, HttpResponse, redirect
from .models import Vacancy
from .models import Company
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import VacancyForm
from .forms import VacancyEditForm
from .forms import CompanyForm
from .forms import CompanyEditForm

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

def search(request):
    word = request.GET["keyword"]
    vacancy_list = Vacancy.objects.filter(title__contains=word)
    context = {"vacancies": vacancy_list}
    return render(request, 'vacancy_list.html', context)


def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Неверный логин или пароль")

    return render(request, 'auth/sign_in.html')


def sign_out(request):
    logout(request)
    return redirect(sign_in)



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
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    context = {"vacancies": vacancies}
    # context["example"] = "hello"
    return render(request, 'vacancy/vacancy_list.html', context)

def vacancy_detail(request, id):
    vacancy_object = Vacancy.objects.get(id=id)  # 1
    candidates = vacancy_object.candidate.all()  # list
    context = {
        'vacancy': vacancy_object,
        'candidates_list': candidates,
    }
    return render(request, 'vacancy/vacancy_detail.html', context)

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

def vacancy_edit_df(request, id):
    vacancy_object = Vacancy.objects.get(id=id)

    if request.method == "GET":
        form = VacancyEditForm(instance=vacancy_object)
        return render(request, "vacancy/vacancy_edit_django_form.html", {"form": form})

    elif request.method == "POST":
        form = VacancyEditForm(data=request.POST, instance=vacancy_object)
        if form.is_valid():
            obj = form.save()
            return redirect(vacancy_detail, id=obj.id)
        else:
            return HttpResponse("Форма не валидна")

def company_list(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    return render(request, 'company/company_list.html', context)

def company_info(request, id):
    company_object = Company.objects.get(id=id)
    return render(
        request, 'company/company_detail.html',
        {'company': company_object}
    )

def company_add_form(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            new_company = form.save()
            return redirect(f'/company/{new_company.id}/')
    company_form = CompanyForm()
    return render(
        request,
        'company/company_add_form.html',
        {"company_form": company_form}
    )

def company_edit(request, id):
    company_object = Company.objects.get(id=id)

    if request.method == "GET":
        form = CompanyEditForm(instance=company_object)
        return render(request, "company/company_edit_form.html", {"form": form})

    elif request.method == "POST":
        form = CompanyEditForm(data=request.POST, instance=company_object)
        if form.is_valid():
            obj = form.save()
            return redirect(company_info, id=obj.id)
        else:
            return HttpResponse("Форма не валидна")
