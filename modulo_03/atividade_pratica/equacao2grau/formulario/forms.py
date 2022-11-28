from django import forms
from .models import Equacao

# modelForm
class EquacaoForm(forms.ModelForm):
  class Meta:
    model = Equacao
    fields = ['coeficienteA', 'coeficienteB', 'coeficienteC']