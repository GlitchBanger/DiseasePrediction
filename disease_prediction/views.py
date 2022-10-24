from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from .apps import Predictor
from django.forms.models import model_to_dict
from .forms import LoginForm, RegistrationForm, TestForm
from .models import LoginDetails, UserData
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
    

def test(request, id):
    form = TestForm()
    rendered = form.render('disease_prediction/test_form.html')
    return render(request, 'disease_prediction/user.html', {
        'test': True,
        'id': id,
        'form': rendered
    })
   
def result(request, id):
    if request.method == 'POST':
    	form = TestForm(request.POST)
    	data = []
    	if form.is_valid():
    	    for i in form.cleaned_data.keys():
    	        if form.cleaned_data[i]:
    	    	    data.append(1)
    	        else:
    	            data.append(0)
    	data.append(0)
    	user = LoginDetails.objects.get(id = id)
    	pred = Predictor(app_name = 'disease_prediction', app_module = 'apps')
    	prediction = pred.prediction([data])[0][0][0]
    	percentage = round(max(pred.prediction([data])[1][0]) * 100)
    	userdata = user.userdata_set.create(prediction = prediction, percentage = percentage)
    	records = form.save(commit = False)
    	records.user_id = userdata.id
    	records.save()
    	return render(request, 'disease_prediction/results.html',{'prediction': prediction, 
    								   'percentage': percentage,
    								   'id': id}) 
    								 
def records(request, id):
    userdata = UserData.objects.get(id = id)
    records = model_to_dict(userdata.records_set.all()[0])
    record_cleaned = {}
    for key in records.keys():
    	if key == 'user':
    	    continue
    	name = ' '.join(key.split('_'))
    	name = name.replace(name[0], name[0].upper(), 1)
    	if records[key]:
    	    val = 'True'
    	else:
    	    val = 'False'
    	record_cleaned[name] = val
    return render(request, 'disease_prediction/records.html', {
    					'records' : record_cleaned,
    					'id' : userdata.user.id
    			    })

