from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class SeForm(forms.Form):
    CHOICES_TYPE = (('presente', 'Presente'), ('pasado', 'Pasado'))
    CHOICES_CANTIDAD = ((100, '100'), (500, '500'), (1000, '1000'))
    busqueda =  forms.CharField(label="Busqueda*", widget=forms.TextInput(attrs={'placeholder':'Busqueda', 'class':'from-control'}))
    tipo =  forms.ChoiceField(label="Tipo*", widget=forms.RadioSelect, choices=CHOICES_TYPE)
    cantidad = forms.ChoiceField(label="Cantidad*", choices=CHOICES_CANTIDAD)
    fecha_inicio = forms.DateField(required=False, label="Fecha de inicio", widget = AdminDateWidget)
    fecha_fin = forms.DateField(required=False, label="Fecha de termino", widget = AdminDateWidget)
