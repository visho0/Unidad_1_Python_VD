from django import forms
from .models import Dispositivo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ['nombre', 'categoria', 'zona', 'consumo_maximo']

        def clean_nombre(self):
            nombre = self.cleaned_data.get('nombre')
            if len(nombre) < 3:
                raise forms.ValidationError("El nombre debe tener almenos 3 caracteres")
            return nombre