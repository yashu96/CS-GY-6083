from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        if len(cd['password']) < 8:
            raise forms.ValidationError('Password is less than 8 letters')
        if cd['password'].isalnum()!=True:
            raise forms.ValidationError('Passwords should have a number')
        if cd['password'].islower():
            raise forms.ValidationError('Passwords should have a capital letter')    
        return cd['password']

    # def validate(self):
    #     cd= self.cleaned_data
    #     while True:
    #         if len(cd['password']) < 8:
    #             raise forms.ValidationError('Passwords is less than 8 letters')

    #         elif re.search('[0-9]',cd['password']) is None:
    #             raise forms.ValidationError('Passwords should have a number')
 
    #         elif re.search('[A-Z]',cd['password']) is None: 
    #             raise forms.ValidationError('Passwords should have a capital letter')
    #     return cd['password']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
