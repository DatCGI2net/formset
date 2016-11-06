
#from django.db import models
from django import forms

from django.forms.models import inlineformset_factory

from setup.models import Setup, Specification

SetupSpecFormSet = inlineformset_factory(Setup,Specification,
                                         fields=('result', ),
                                         extra=2
                                         )
    
class SetupForm(forms.ModelForm):
    class Meta:
        model = Setup
        fields = '__all__'

class SpecificationForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = '__all__'
        
        