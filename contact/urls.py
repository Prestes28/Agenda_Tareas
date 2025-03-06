from django.urls import path
from . import views
urlpatterns = [
    path('crud/', views.crud, name='list'),
    path('contact/',views.form, name='form'),
    path('edit_contact/<int:contact_id>/', views.edit_contact, name="edit_contact"),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact')
    
]
