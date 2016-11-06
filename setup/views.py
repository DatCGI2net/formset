#from django.shortcuts import render, HttpResponseRedirect
from setup.forms import SetupSpecFormSet, SetupForm
from setup.models import Setup
from django.views.generic import ListView, DetailView, CreateView

class IndexListView(ListView):
    
    template_name = 'setup/index.html'
    context_object_name = 'setups'
    
    def get_queryset(self):
        
        return Setup.objects.all()
    
    #return render(request, 'setup/index.html', {'setups': setups})
class CreateView(CreateView):
    
    model = Setup
    template_name = 'setup/setup.html'
    form_class = SetupForm
    
    def get(self, request, *args, **kwargs):
        
        self.object = None
        form = self.form_class(self.object)
        setupspec_formset = SetupSpecFormSet(instance=self.object)
        
        context = self.get_context_data(form=form, details=setupspec_formset)
        return self.render_to_response(context)
       
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class(request.POST)
        ##self.object = self.get_object()
        
        if form.is_valid():
            self.object = setup = form.save(commit=False)
            detail_form = SetupSpecFormSet(request.POST, instance=self.object)
            if detail_form.is_valid():
                
                setup = form.save()
                detail_form.save()
                print 'setup:', setup.description, ' : vs ', self.object.description
            
            
        else:
            detail_form = SetupSpecFormSet(request.POST, instance=self.object)
            
        context = self.get_context_data(form=form, details=detail_form)
        return self.render_to_response(context)
        
class EditView(DetailView):    

    model = Setup
    template_name = 'setup/setup.html'
    form_class = SetupForm
    
    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        form = self.form_class(self.object)
        setupspec_formset = SetupSpecFormSet(instance=self.object)
        
        context = self.get_context_data(form=form, details=setupspec_formset)
        return self.render_to_response(context)
       
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        self.object = self.get_object()
        detail_form = SetupSpecFormSet(request.POST, instance=self.object)
        if form.is_valid() and detail_form.is_valid():
            detail_form.save()
            setup = form.save()
            print 'setup:', setup.description, ' : vs ', self.object.description
            
            
        
        context = self.get_context_data(form=form, details=detail_form)
        return self.render_to_response(context)
    
    
    