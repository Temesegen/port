from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    abouts = About.objects.get(id=1)
    services = service.objects.all()
    contacts = contactform()
    works = work.objects.all()

    if request.method == 'POST':
        contacts = contactform(request.POST)

        if contacts.is_valid():
            #   email = contacts.cleaned_data['email']
            #   subject = contacts.cleaned_data['subject']
            #   message = contacts.cleaned_data['message']
              contacts.save()
              return redirect('home')
                    
    else:
        contacts=contactform()
            

    
    return render(request,'index.html',{'about':abouts,'services':services, 'contacts':contacts, 'works':works})
