from django import forms

class TorneoForm(forms.Form):
    nombre=forms.CharField(max_length=50)

class ArbitroForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()

class EquipoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    jugadores=forms.IntegerField()