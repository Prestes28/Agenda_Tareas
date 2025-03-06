from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['user']
        labels={
            'name':'Nombre',
            'last_name':'Apellido',
            'company':'compania'
        }
        error_messages = {
            "name": {
                "max_length": ("Este campo es muy largo."),
            },
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning'}),
            'last_name': forms.TextInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning'}),
            'tel1': forms.TextInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning'}),
            'tel2': forms.TextInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning'}),
            'company':forms.SelectMultiple(attrs={'class':'form-select  bg-secondary border border-2 text-white border-warning'}, choices={
    '':'Ninguno',
    'Movistar':'Movistar',
    'Claro':'Claro',
    'Personal':'Personal',
    'Tuenti':'Tuenti'
    })

                 }