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
            'company':'Compania',
            'tel2':'Tel2 (Opcional)'
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
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.label_suffix = ''  # Opcional, para quitar los ":" después del label
                field.widget.attrs['aria-label'] = field.label  # Accesibilidad (opcional)
                # Guardar la clase CSS del label en un atributo del campo
                field.label_classes = 'form-label text-warning mt-2'