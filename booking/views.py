from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request=request, template_name='booking/index.html')
def elements(request):
    return render(request=request, template_name='booking/elements.html')
def hotels(request):
    return render(request=request, template_name='booking/hotels.html')
def insurance(request):
    return render(request=request, template_name='booking/insurance.html')
def packages(request):
    return render(request=request, template_name='booking/packages.html')
def about(request):
    return render(request=request, template_name='booking/about.html')
def bloghome(request):
    return render(request=request, template_name='booking/blog-home.html')
def login(request):
    return render(request=request, template_name='booking/login.html')
def register(request):
    return render(request=request, template_name='booking/register.html')
def search(request):
    return render(request=request, template_name='booking/search.html')
def book(request):
    return render(request=request, template_name='booking/book.html')
def booking(request):
    return render(request=request, template_name='booking/booking.html')
def layout(request):
    return render(request=request, template_name='booking/layout.html')
def indexbk(request):
    return render(request=request, template_name='booking/indexbk.html')
def layout2(request):
    return render(request=request, template_name='booking/layout.html')