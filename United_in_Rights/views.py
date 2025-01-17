from django.shortcuts import render,redirect
from django.contrib import messages
from United_in_Rights.models import Client
from United_in_Rights.models import Victim

def index(request):
    return render(request, 'index.html')

def education(request):
    return render(request, 'gbvEducation.html')

def report(request):
    return render(request, 'report.html')

def victims_list(request):
    if request.method == "POST":

        victim_name = request.POST['victim_name']
        victim_email = request.POST['victim_email']
        victim_address = request.POST['victim_address']
        contact_subject = request.POST['contact_subject']
        victim_message = request.POST['victim_message']

        

        victim = Victim(
            victim_name=victim_name,
            victim_email=victim_email,
            victim_address=victim_address,
            contact_subject=contact_subject,
            victim_message=victim_message,
        )

        victim.save()
        return redirect('home')

    return render(request, 'index.html')

def view_victims(request):
    victims = Victim.objects.all()
    return render(request, 'victims.html', {'victims': victims})

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        victim_name = request.POST['victim_name']
        victim_email = request.POST['victim_email']
        victim_address = request.POST['victim_address']
        contact_subject = request.POST['contact_subject']
        victim_message = request.POST['victim_message']

        victim = Victim(
            victim_name=victim_name,
            victim_email=victim_email,
            victim_address=victim_address,
            contact_subject=contact_subject,
            victim_message=victim_message
        )

        victim.save()
        return redirect('home')

    return render(request, 'register.html')





def clients_list(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_address = request.POST['email_address']
        telephone_number = request.POST['telephone_number']

        client = Client(
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            telephone_number=telephone_number,


        )

        client.save()
        # return redirect('home')

        return render(request, 'clients.html')

    def view_clients(request):
        clients = client.objects.all()
        return render(request, 'clients.html', {'clients': clients})


    

# Create your views here.
