from django.shortcuts import render, redirect
from .models import Contact, Email, Files
from .forms import ContaactForm, EmailForm, DocumentForm
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
    if 'update' in request.POST:
        form = ContaactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
        if not form.is_valid():
            error = "invalid data provided in form"
            return render(request, 'contacts/contactdetail.html', {'contact': contact, 'form': form, 'error': error})
    if 'delete' in request.POST:
        contact.delete()
        return redirect('home')
    return render(request, 'contacts/contactdetail.html', {'contact': contact, 'form': form})

def EmailPage(request):
    emails = Email.objects.all()
    form = EmailForm()
    return render(request, 'emails/emailpage.html', {'emails': emails, 'form': form})

def DocumentsPage(request):
    files = Files.objects.all()
    form = DocumentForm()
    return render(request, 'documents/documentspage.html', {'files': files, 'form': form})





