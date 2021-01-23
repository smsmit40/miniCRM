from django.forms import ModelForm
from .models import Contact

class ContaactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'