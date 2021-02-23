from django.shortcuts import render, HttpResponse, redirect

from .models import Dojo, Ninja
# Create your views here.

def index(request):
    context = {
        'dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def create_dojo(request):
    Dojo.objects.create(
        name = request.POST['dojo_name'],
        city = request.POST['city'],
        state = request.POST['state'],
    )
    return redirect('/')

def create_ninja(request):
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo_id = Dojo.objects.get(id= request.POST['dojo_id']),
    )
    return redirect('/')