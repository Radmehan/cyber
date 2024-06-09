from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from myapp.models import Contact, Schedule, MultipleOfThreeField
from django.contrib.auth import logout
from django.db import connection 
from .decorators import admin_required 


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
        accept = request.POST.get('accept', 'no') == 'yes'
        contact = Contact(name=name, address=address, contact=contact, email=email, subject=subject, message=message, accept=accept)
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
        schedule.schedule_id = MultipleOfThreeField().pre_save(schedule, True)

        if schedule.schedule_id <= 4:
            schedule.save()

        id = schedule.schedule_id
        if id <= 4:
            messages.success(request, f"Thanks for book an appoinment. Your apponit number is {id}")
        else:
            messages.error(request, f"Thanks for book an appoinment. But, your apponit number is out of range")
        return redirect('/')
    
    else:
        return HttpResponse('404-not found')
    

@admin_required
def reset_msg_id(request):
    if request.method=='GET':
      # Delete all records in the Patient model.
      Schedule.objects.all().delete()

      # Reset the auto-increment value for the msg_id field to 3.
      with connection.cursor() as cursor:
         cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'myapp';")

      # Redirect the user back to the home page.
      messages.success(request,"Previous patient's ids are deleted successfully")
      return redirect('/')


def logoutHandle(request):
  if request.method=='GET':
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('/')
