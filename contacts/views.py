from django.shortcuts import render
from .models import Contact
from .forms import ContaactForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def contacts(request):
    contactslist = Contact.objects.all()
    form = ContaactForm()
    return render(request, 'contacts/contacts.html', {'contacts': contactslist, 'form': form})

def contactdetail(request, pk):
    contact = Contact.objects.get(pk=pk)
    form = ContaactForm(instance=contact)
    return render(request, 'contacts/contactdetail.html', {'contact': contact, 'form': form})

