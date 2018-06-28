from django import forms
class student(forms.Form):
    username=forms.CharField(label="username",max_length=100)
    email=forms.EmailField()
    Password1=forms.CharField(label="Password",max_length=20)
    Password2=forms.CharField(label="Password",max_length=20)
