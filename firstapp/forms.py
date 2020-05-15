from django import forms
from firstapp.models import ModelForm,MyModel,GeneralRemedies,AuyervedicRemedies,HomeopathicRemedies

class FormName(forms.ModelForm):
    #Name=forms.CharField()
    #Email=forms.EmailField()
    class Meta:
        model=ModelForm
        fields='__all__'

class MyModel(forms.ModelForm):
    

    class Meta:
        model = MyModel
        fields="__all__"
        widgets = {'Symptoms': forms.CheckboxSelectMultiple}

class GeneralRemedies(forms.ModelForm):

    class Meta:
        model=GeneralRemedies
        fields="__all__"        
class AuyervedicRemedies(forms.ModelForm):

    class Meta:
        model=AuyervedicRemedies
        fields="__all__"               

class HomeopathicRemedies(forms.ModelForm):

    class Meta:
        model=HomeopathicRemedies
        fields="__all__"                       