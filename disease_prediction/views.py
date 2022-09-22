from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from .apps import Predictor
from .forms import LoginForm, RegistrationForm
from .models import LoginDetails
# Create your views here.

def index(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        form_render = form.render('disease_prediction/login_form.html')
        if form.is_valid():
            return HttpResponseRedirect('user/' + form.id + '/')
        else:
            return render(request, 'disease_prediction/login.html', {'form': form_render})
            
    form = LoginForm().render('disease_prediction/login_form.html')
    return render(request, 'disease_prediction/login.html', {'form': form})
    
    
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        form_render = form.render('disease_prediction/login_form.html')
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'disease_prediction/registration.html', {'form': form_render})
    form = RegistrationForm().render('disease_prediction/login_form.html')
    return render(request, 'disease_prediction/registration.html', {'form': form})

    
def user(request, id):
    userdata = LoginDetails.objects.get(id = id)
    return render(request, 'disease_prediction/user.html', {
        'logindetail': [i for i in userdata.userdata_set.all()],
        'id' : id
    })
        
