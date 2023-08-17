from django import forms


from django.contrib.auth.models import  User

class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True,
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "username", "placeholder": "username"}
        ),
    )
    

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "example@juacalo.com",
            }
        ),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "password"}),
    )
    password2 = forms.CharField(label='confirmar password',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'
                                    })) 
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso nde mykure')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El Email tambien ya se encuentra en uso nde mykure')
        return email

