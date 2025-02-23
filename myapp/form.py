from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm,forms
from django.contrib.auth.models import User
from myapp.models import Customer

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control','Placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

class RegistrationForm(UserCreationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),required=True)
     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)

     class Meta:
          model=User
          fields = ['username','email','password1','password2']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'OldPassword'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'NewPassword1'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'NewPassword2'}))

class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs=  {'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs=  {'autocomplete':'current-password','class':'form-control'}))



class CustomerProfileForm(forms.ModelForm):
     class Meta:
          model = Customer
          fields = ['name','locality','city','mobile','state','zipcode']
          widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'locality': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Locality'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your City'}),
            'mobile': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Mobile.No'}),
            'state': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your State'}),
            'zipcode': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Zipcode'}),
          }


