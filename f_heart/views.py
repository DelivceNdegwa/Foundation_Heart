from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

from .forms import InquiriesForm, MembersOfProgramForm
from .models import Inquiries, MembersOfProgram
from Foundation_Heart.keys import user_email as email_to

def our_programs(request):

    return render(request, 'our_programs.html')

def index(request):
    if request.method == 'GET':
        form = InquiriesForm()
    else:
        form = InquiriesForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:          
                send_mail(
                    name,
                    message,
                    email_to,
                    [email],
                    fail_silently=False
                )

                form.save()
                messages.success(request, 'Your inquiry has been made, you will receive feedback shortly.')

            except BadHeaderError:
                messages.warning(request, 'The message you wrote is invalid.')

    context = {
                'form' : form,
                'data' : Inquiries.objects.all()
            }

    return render(request, 'f_heart/index.html', context)

def about_us(request):

    return render(request, 'f_heart/about_us.html',{})

def our_programs(request):

    return render(request, 'f_heart/our_programs.html', {})

def register(request):
    if request.method == 'GET':
        form = MembersOfProgramForm()

    else:
        form = MembersOfProgramForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            
            form.save()

            messages.success(request, 'Congratulations '+first_name+', you have successfully registered for our programs. You will receive an email shortly!')

            send_mail(
                'Thank you '+first_name+'!',
                'Hello '+last_name+'! We are excited that you are enrolling for our programs. You are now part of us :)',
                email_to,
                [email],
                fail_silently= False,
            )

    context = {
        'form': form
    }

    return render(request, 'f_heart/program_registration.html', context)

def messages(request):

    return render(request, 'f_heart/messages.html', {})