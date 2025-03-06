from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields =['username','email','password1','password2']
        labels={
            'username':'Nombre de usuario',
            'email':'Email',
            'password1':'Contraseña',
            'password2':'Confirmar Contraseña',
        }
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        css_class = 'form-control bg-secondary border border-2 text-white border-warning'
        for field_name, field in self.fields.items():
            field.label_suffix = ''
            field.widget.attrs['aria-label'] = field.label
            field.label_classes = 'form-label text-warning mt-2'
            field.widget.attrs['class'] = css_class