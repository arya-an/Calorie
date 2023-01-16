from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App.models import *


class NewUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','password1','password2']
       
        
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for field_name in ('username','password1','password2'):
            self.fields[field_name].help_text = ''
            
            
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['item_name','calories','protein','carbs']
       
        
class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['activity_name','burnout_cal']
        
        
class UserFoodForm(forms.ModelForm):
    class Meta:
        model = UserFood
        fields = ['fooditem','fintake','activity','ahours']
        