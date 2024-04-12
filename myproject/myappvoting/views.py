from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from .models import Contact, Voter


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def thank_you(request):
    return render(request, 'thanku.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return HttpResponseRedirect('contact/success/')  
    else:
        return render(request, 'contact.html')

def Privacy_Policy(request):
    return render(request, 'privacy_policy.html')





def vote(request):
    if request.method == 'POST':
        try:
            aadhar_value = request.POST.get('aadhar')
            vote_value = request.POST.get('vote')
            print("working this is ")
            print(aadhar_value, vote_value)

            voter = Voter(aadhar=aadhar_value, vote=vote_value)
            voter.save()

            
        except IntegrityError:
            messages.error(request, 'Error: Your vote could not be cast. Please make sure you have not already voted.')
            return HttpResponseRedirect('/vote') 
        return HttpResponseRedirect('/contact/success') 
    else:
        return render(request, 'vote.html')
