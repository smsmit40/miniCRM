from django.shortcuts import render, redirect
from .models import Contact, Email, Files, Reminder
from .forms import ContaactForm, EmailForm, DocumentForm, ReminderForm
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

def EmailDetail(request, pk):
    emails = Email.objects.get(pk=pk)
    form = EmailForm(instance=emails)

    if 'update' in request.POST:
        form = EmailForm(request.POST, instance=emails)
        if form.is_valid():
            form.save()
            return redirect('home')
    if 'delete' in request.POST:
        emails.delete()
        return redirect('home')
    return render(request, 'emails/emaildetail.html', {'form': form})

def DocumentsPage(request):
    files = Files.objects.all()
    form = DocumentForm()
    if 'add' in request.POST:
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "invalid"
            return render(request, 'documents/documentspage.html', {'files': files, 'form': form, 'error': error})
    return render(request, 'documents/documentspage.html', {'files': files, 'form': form})

def documentsdetail(request, pk):
    document = Files.objects.get(pk=pk)
    form = DocumentForm(instance=document)
    return render(request, 'documents/documentsdetail.html', {'form': form})

def ReminderPage(request):
    reminder = Reminder.objects.all()
    form = ReminderForm()
    return render(request, 'reminders/reminderspage.html', {'reminder': reminder, 'form': form})





