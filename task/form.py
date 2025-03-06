from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']
        labels= {
            'title':'Titulo',
            'short_description':'Descripción corta',
            "description":"Descripción",
            "date":"Fecha",
            'active':'Activo'
        }
        error_messages ={
            'title':{
                'max_length':('Este campo es muy largo.'),
                'blank':('Este campo no puede ser nulo'),
                'null':('Este campo no puede ser nulo')
            },
            'short_description':{
                'max_length':('Este campo es muy largo.'),
                'blank':('Este campo no puede ser nulo'),
                'null':('Este campo no puede ser nulo')
            }
        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning mt-2'}),
            'short_description':forms.TextInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning mt-2'}),
            'description':forms.Textarea(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning mt-2'}),
            'date':forms.DateInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning mt-2 ','type':'date'}),
            'active':forms.CheckboxInput(attrs={'class':'form-check-input bg-secondary border border-2 text-white border-warning mt-2'})
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.label_suffix = ''  # Opcional, para quitar los ":" después del label
                field.widget.attrs['aria-label'] = field.label  # Accesibilidad (opcional)
                # Guardar la clase CSS del label en un atributo del campo
                field.label_classes = 'form-label text-warning mt-2'