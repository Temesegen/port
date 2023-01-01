from django import forms
from django.forms import ModelForm
from .models import *

class contactform(forms.ModelForm):
        class Meta:
               model = contact
               fields = '__all__'

        def __str__(self):
                return self.name
        # def save(self, commit=True):
        #       user = super(contact, self).save(commit=False)
        #       user.name = self.cleaned_data['name']
        #       user.email = self.cleaned_data['email']
        #       user.subject = self.cleaned_data['subject']
        #       user.message = self.cleaned_data['message']
        #       if commit:
        #              user.save()
        #              return user
 
    
        
        
            
            
