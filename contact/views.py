from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import ContactForm
from .models import Contact


@login_required
def form(request):
    form= ContactForm()
    return render(request, 'contact_form.html',{'form': form})

@login_required
def crud(request):
    if request.method =='GET':
        form = ContactForm()
        contacts = Contact.objects.filter(user=request.user)
        return render(request,'index.html', {'form': form, 'contacts':contacts})
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact =form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('list')
        else:
            print('Algo salio mal')
            print(request.POST)
            return render(request,'index.html', {'form': form})

@login_required   
def edit_contact(request, contact_id):
    edit = contact_id
    contact = Contact.objects.get(id=edit)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('list')
    else:
        form = ContactForm(instance=contact)
    
    return render(request,'edit_contact.html',{'form':form , 'contact': contact})

@login_required
def delete_contact(request,contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('list')