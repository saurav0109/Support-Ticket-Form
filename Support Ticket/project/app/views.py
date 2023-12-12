from django.shortcuts import render
from .models import *
def supportticket(request):
    if request.method == "POST":
        fname = request.POST['fname']  #getting the information from the frontend i.e firstname,lastname etc
        lname = request.POST['lname']
        department = request.POST['department']
        problem = request.POST['problem']
        image = request.POST['avatar']
        new_ticket = Support_Ticket.objects.create(fname=fname,lname=lname,department=department,problem=problem,image=image)
         
        
        #new_ticket is used to create a new object of the Support_Ticket model to issue a new ticket
    return render(request,'Support_ticket_form.html')
