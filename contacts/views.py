from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contacts(request):
    contactslist = Contact.objects.all()
    return render(request, 'contacts/contacts.html', {'contacts': contactslist})

