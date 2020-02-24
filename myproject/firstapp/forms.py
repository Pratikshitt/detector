from django import forms
from firstapp.models import ModelForm,MyModel,Remedies

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

# class Remedies(forms.ModelForm):

#     class Meta:
#         model=Remedies
#         fields="_all__"        