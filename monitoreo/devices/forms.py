from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'category', 'zone', 'max_consumption', 'organization']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("The name must have at least 3 characters")
        return name
