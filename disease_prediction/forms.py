from django import forms
from django.forms import ModelForm, Form
from .models import LoginDetails
from django import forms
from django.contrib.auth.hashers import make_password, check_password
import re

class LoginForm(ModelForm):
    id = None;
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
        
        
class TestForm(Form):
    itching = forms.BooleanField()
    skin_rash = forms.BooleanField()
    nodal_skin_eruptions = forms.BooleanField()
    continuous_sneezing = forms.BooleanField()
    shivering = forms.BooleanField()
    chills = forms.BooleanField()
    joint_pain = forms.BooleanField()
    stomach_pain = forms.BooleanField()
    acidity = forms.BooleanField()
    ulcers_on_tongue = forms.BooleanField()
    muscle_wasting = forms.BooleanField()
    vomiting = forms.BooleanField()
    burning_micturition = forms.BooleanField()
    spotting_urination = forms.BooleanField()
    fatigue = forms.BooleanField()
    weight_gain = forms.BooleanField()
    anxiety = forms.BooleanField()
    cold_hands_and_feets = forms.BooleanField()
    mood_swings = forms.BooleanField()
    weight_loss = forms.BooleanField()
    restlessness = forms.BooleanField()
    lethargy = forms.BooleanField()
    patches_in_throat = forms.BooleanField()
    irregular_sugar_level = forms.BooleanField()
    cough = forms.BooleanField()
    high_fever = forms.BooleanField()
    sunken_eyes = forms.BooleanField()
    breathlessness = forms.BooleanField()
    sweating = forms.BooleanField()
    dehydration = forms.BooleanField()
    indigestion = forms.BooleanField()
    headache = forms.BooleanField()
    yellowish_skin = forms.BooleanField()
    dark_urine = forms.BooleanField()
    nausea = forms.BooleanField()
    loss_of_appetite = forms.BooleanField()
    pain_behind_the_eyes = forms.BooleanField()
    back_pain = forms.BooleanField()
    constipation = forms.BooleanField()
    abdominal_pain = forms.BooleanField()
    diarrhoea = forms.BooleanField()
    mild_fever = forms.BooleanField()
    yellow_urine = forms.BooleanField()
    yellowing_of_eyes = forms.BooleanField()
    acute_liver_failure = forms.BooleanField()
    fluid_overload = forms.BooleanField()
    swelling_of_stomach = forms.BooleanField()
    swelled_lymph_nodes = forms.BooleanField()
    malaise = forms.BooleanField()
    blurred_and_distorted_vision = forms.BooleanField()
    phlegm = forms.BooleanField()
    throat_irritation = forms.BooleanField()
    redness_of_eyes = forms.BooleanField()
    sinus_pressure = forms.BooleanField()
    runny_nose = forms.BooleanField()
    congestion = forms.BooleanField()
    chest_pain = forms.BooleanField()
    weakness_in_limbs = forms.BooleanField()
    fast_heart_rate = forms.BooleanField()
    pain_during_bowel_movements = forms.BooleanField()
    pain_in_anal_region = forms.BooleanField()
    bloody_stool = forms.BooleanField()
    irritation_in_anus = forms.BooleanField()
    neck_pain = forms.BooleanField()
    dizziness = forms.BooleanField()
    cramps = forms.BooleanField()
    bruising = forms.BooleanField()
    obesity = forms.BooleanField()
    swollen_legs = forms.BooleanField()
    swollen_blood_vessels = forms.BooleanField()
    puffy_face_and_eyes = forms.BooleanField()
    enlarged_thyroid = forms.BooleanField()
    brittle_nails = forms.BooleanField()
    swollen_extremeties = forms.BooleanField()
    excessive_hunger = forms.BooleanField()
    extra_marital_contacts = forms.BooleanField()
    drying_and_tingling_lips = forms.BooleanField()
    slurred_speech = forms.BooleanField()
    knee_pain = forms.BooleanField()
    hip_joint_pain = forms.BooleanField()
    muscle_weakness = forms.BooleanField()
    stiff_neck = forms.BooleanField()
    swelling_joints = forms.BooleanField()
    movement_stiffness = forms.BooleanField()
    spinning_movements = forms.BooleanField()
    loss_of_balance = forms.BooleanField()
    unsteadiness = forms.BooleanField()
    weakness_of_one_body_side = forms.BooleanField()
    loss_of_smell = forms.BooleanField()
    bladder_discomfort = forms.BooleanField()
    foul_smell_of_urine = forms.BooleanField()
    continuous_feel_of_urine = forms.BooleanField()
    passage_of_gases = forms.BooleanField()
    internal_itching = forms.BooleanField()
    toxic_look_typhos = forms.BooleanField()
    depression = forms.BooleanField()
    irritability = forms.BooleanField()
    muscle_pain = forms.BooleanField()
    altered_sensorium = forms.BooleanField()
    red_spots_over_body = forms.BooleanField()
    belly_pain = forms.BooleanField()
    abnormal_menstruation = forms.BooleanField()
    dischromic_patches = forms.BooleanField()
    watering_from_eyes = forms.BooleanField()
    increased_appetite = forms.BooleanField()
    polyuria = forms.BooleanField()
    family_history = forms.BooleanField()
    mucoid_sputum = forms.BooleanField()
    rusty_sputum = forms.BooleanField()
    lack_of_concentration = forms.BooleanField()
    visual_disturbances = forms.BooleanField()
    receiving_blood_transfusion = forms.BooleanField()
    receiving_unsterile_injections = forms.BooleanField()
    coma = forms.BooleanField()
    stomach_bleeding = forms.BooleanField()
    distention_of_abdomen = forms.BooleanField()
    history_of_alcohol_consumption = forms.BooleanField()
    fluid_overload = forms.BooleanField()
    blood_in_sputum = forms.BooleanField()
    prominent_veins_on_calf = forms.BooleanField()
    palpitations = forms.BooleanField()
    painful_walking = forms.BooleanField()
    pus_filled_pimples = forms.BooleanField()
    blackheads = forms.BooleanField()
    scurring = forms.BooleanField()
    skin_peeling = forms.BooleanField()
    silver_like_dusting = forms.BooleanField()
    small_dents_in_nails = forms.BooleanField()
    inflammatory_nails = forms.BooleanField()
    blister = forms.BooleanField()
    red_sore_around_nose = forms.BooleanField()
    yellow_crust_ooze = forms.BooleanField()
