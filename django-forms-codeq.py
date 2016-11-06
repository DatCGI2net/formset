""" For the following many->one relationship (Specification(n)->Setup), 
    write snippets for the following:

    1. Create a formset relating the models via their form classes
    2. Write a simple Django view controller that handles a POST to 
       the form & formset that validates and saves data into both 
       tables from request.POST values.
"""

from django.db import models
from django import forms

class Setup(models.Model):
    description = models.CharField(max_length=100)
    
class Specification(models.Model):
    setup = models.ForeignKey(Setup, related_name="target_specs")
    result = models.FloatField(default=0.)
    
class SetupForm(forms.ModelForm):
    class Meta:
        model = Setup
        fields = '__all__'

class SpecificationForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = '__all__'


## use inline formset        
from django.forms.models import inlineformset_factory


SetupSpecFormSet = inlineformset_factory(Setup,Specification,
                                         fields=('result', ),
                                         extra=2
                                         )
                                         
##views                                         
def setup(request):
    
    
    if request.POST:
        
        form = SetupForm(request.POST)
        if form.is_valid():
            setup = form.save(commit=False)
            setupspec_formset = SetupSpecFormSet(request.POST, instance=setup)
            if setupspec_formset.is_valid():
                
                setup.save()
                spec = setupspec_formset.save()
                print 'setup:', setup.id, 'spec:', spec
                return  HttpResponseRedirect('/')
    else:
        
        form = SetupForm()
        
        setupspec_formset = SetupSpecFormSet(instance=Setup())

    return render(request, 'setup/setup.html', {'form': form,
                                              'details': setupspec_formset})
    