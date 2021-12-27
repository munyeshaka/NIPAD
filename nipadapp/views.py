from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import*
from django.http import JsonResponse

# Create your views here.

def home(request):
    #upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')
     #upcoming variable receives data from db witch is not expired
    return render(request, 'nipadapp/home.html')

def propos(request):
    return render(request, 'nipadapp/propos.html')

def regions(request):
    return render(request, 'nipadapp/regions.html')

def program(request):
    return render(request, 'nipadapp/program.html')

def rejoindre(request):
    return render(request, 'nipadapp/rejoindre.html')

def contactes(request):
    return render(request, 'nipadapp/contactes.html')

def services(request):
    return render(request, 'nipadapp/services.html')

class CutomerNumJsonView(View):
    def get(self, *args, **kwargs):
        customer_count = Customer.objects.filter(active=True).count()
        return JsonResponse({'customer_count':customer_count})
