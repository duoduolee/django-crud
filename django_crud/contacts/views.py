from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact
from django.urls import reverse_lazy



class ContactList(ListView): 
    model = Contact

class ContactDetail(DetailView): 
    model = Contact



class ContactCreate(CreateView): 
    model = Contact
    fields = '__all__'
    success_url = reverse_lazy('contact_list')

	

class ContactUpdate(UpdateView): 
    model = Contact
    fields = '__all__'
    success_url = reverse_lazy('contact_list')

class ContactDelete(DeleteView): 
    model = Contact
    success_url = reverse_lazy('contact_list')
