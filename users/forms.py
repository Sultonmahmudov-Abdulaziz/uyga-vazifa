from django import forms
from .models import User



class LoginForm(forms.Form):

    username = forms.CharField(required=True,widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class": "form-control"}))



     

class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class": "form-control"}))
    confirm_password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class": "form-control"}))



    def clean(self): 
        password=self.cleaned_data.get('password',None)
        confirm_password=self.cleaned_data.get('confirm_password',None)

        if password:
            if confirm_password !=password:
                raise forms.ValidationError("Passwordlar ikki hil")
            

        return self.cleaned_data
    

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    phone_number = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control"}))
    bio = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(required=False,widget=forms.EmailInput(attrs={"class": "form-control"}))
    photo = forms.ImageField(required=False,widget=forms.FileInput(attrs={"class": "form-control"}))


    class Meta:
        model = User
        fields=('username','first_name','last_name','phone_number','bio','email','photo')


    

    

    