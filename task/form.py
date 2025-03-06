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
            'title':forms.TextInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning'}),
            'short_description':forms.TextInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning'}),
            'description':forms.Textarea(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning'}),
            'date':forms.DateInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning','type':'date'}),
            'active':forms.CheckboxInput(attrs={'class':'form-control bg-secondary border border-2 text-white border-warning'})
        }
     