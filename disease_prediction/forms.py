from django import forms
from django.forms import ModelForm, Form
from .models import LoginDetails, Records
from django import forms
from django.contrib.auth.hashers import make_password, check_password
import re

class LoginForm(ModelForm):
    class Meta:
        model = LoginDetails
        fields = ['username', 'password']
        
        
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        
        self.fields['password'].widget = forms.PasswordInput(attrs = {'placeholder' : ''})
        self.fields['password'].widget.attrs['type'] = 'password'
        
        
    def clean(self):
        
        super(LoginForm, self).clean()
        
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if len(password) < 7:
            self._errors['password'] = self.error_class(['The password is atleast 7 characters long'])
            
        try:
            userdata = LoginDetails.objects.get(username = username)
        except LoginDetails.DoesNotExist:
            self._errors['username'] = self.error_class(['The username isn\'t registered'])
            
        if check_password(password, userdata.password) != True:
            self._errors['password'] = self.error_class(['Invalid Password'])
            
        self.id = str(userdata.id)
           
        return self.cleaned_data
        
class RegistrationForm(Form):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    retype = forms.CharField(widget=forms.PasswordInput, label = "Confirm Password")
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
    def save(self):
        
        data = LoginDetails(email = self.cleaned_data.get('email'), 
            username = self.cleaned_data.get('username'),
            password = make_password(self.cleaned_data.get('password')))
            
        data.save()
        
    def clean(self):
    
        super(RegistrationForm, self).clean()
        
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        retype = self.cleaned_data.get('retype')
        
        try:
            userdata = LoginDetails.objects.get(username = username)
            self._errors['username'] = self.error_class(['Username Already Exists'])
        except LoginDetails.DoesNotExist:
            print('Good to go!')
            
        try:
            userdata = LoginDetails.objects.get(email = email)
            self._errors['email'] = self.error_class(['Email Already Exists'])
        except LoginDetails.DoesNotExist:
            print('Good to go!')
        
        
        if password != retype :
            self._errors['retype'] = self.error_class(['Doesn\'t match the given password'])
            
        if len(password) < 7 :
            self._errors['password'] = self.error_class(['Must be atleast 7 characters long'])
            
        return self.cleaned_data
        
        
class TestForm(ModelForm):
    class Meta:
        model = Records
        exclude = ('user',)
