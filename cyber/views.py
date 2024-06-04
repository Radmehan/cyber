from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from myapp.models import Contact, Schedule


def index(request):
    return render(request, 'cyber/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        address = request.POST.get('address','')
        contact = request.POST.get('contact','')
        email = request.POST.get('email','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')

        contact = Contact(name=name, address=address, contact=contact, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, "Thanks for contacting with us we'll back soon.")
        return redirect('/')
        
    
    else:
        return HttpResponse('404-not found')

def schedule(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        address = request.POST.get('address','')
        contact = request.POST.get('contact','')
        email = request.POST.get('email','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')

        schedule = Schedule(name=name, address=address, contact=contact, email=email, subject=subject, message=message)
        schedule.save()
        messages.success(request, "Thanks for book an appoinment.")
        return redirect('/')
    
    else:
        return HttpResponse('404-not found')
