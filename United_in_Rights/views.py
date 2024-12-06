from django.shortcuts import render,redirect
from United_in_Rights.models import Client

def index(request):
    return render(request, 'index.html')

def education(request):
    return render(request, 'gbvEducation.html')

def clients_list(request):
    if request.method == "POST":

        client_name = request.POST['client_name']
        client_email = request.POST['client_email']
        contact_subject = request.POST['contact_subject']
        client_message = request.POST['client_message']

        client = Client(
            client_name=client_name,
            client_email=client_email,
            contact_subject=contact_subject,
            client_message=client_message
        )

        client.save()
        return redirect('registered')

    return render(request, 'index.html')

def view_clients(request):
    clients = Client.objects.all()
    return render(request, 'registered_clients.html', {'clients': clients})

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        client_name = request.POST['client_name']
        client_email = request.POST['client_email']
        contact_subject = request.POST['contact_subject']
        client_message = request.POST['client_message']

        client = Client(
            client_name=client_name,
            client_email=client_email,
            contact_subject=contact_subject,
            client_message=client_message
        )

        client.save()
        return redirect('registered')

    return render(request, 'register.html')

# Create your views here.
