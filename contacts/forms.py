from django.forms import ModelForm
from .models import Contact, Email, Files

class ContaactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = '__all__'

class DocumentForm(ModelForm):
    class Meta:
        model = Files
        fields = '__all__'