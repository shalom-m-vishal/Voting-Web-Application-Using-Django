from django.http import HttpResponse
from django.shortcuts import render
from votingcontact.models import ContactForm
# Create your views here.


def home(request):
    if request.method=='POST':
        contact = ContactForm()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        return HttpResponse("Response Submitted")
    return render(request,'contact.html')