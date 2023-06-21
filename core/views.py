from django.shortcuts import render, HttpResponse

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