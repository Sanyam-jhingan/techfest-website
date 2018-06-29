from django import forms
class student(forms.Form):
    
    required_css_class = 'required'
    
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label="Username",
                                error_messages={'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})
    email = forms.EmailField(label="E-mail")
    Password1 = forms.CharField(widget=forms.PasswordInput,
                                label="Password")
    Password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Password (again)")