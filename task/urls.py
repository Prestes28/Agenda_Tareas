from django.urls import path
from . import views

urlpatterns = [
    path('list_task/', views.listTask, name='listTask'),
    path('form_task/', views.formTask, name='formTask'), 
    path('edit_task/<int:task_id>/', views.editTask, name='editTask'), #incluir despues el <int:task_id>
    path('delete_task/<int:task_id>/', views.deleteTask, name='deleteTask') #incluir despues el <int:task_id>
]
