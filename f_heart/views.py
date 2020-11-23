from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, BadHeaderError

from .forms import InquiriesForm, MembersOfProgramForm
from .models import Inquiries, MembersOfProgram
from Foundation_Heart.keys import user_email as email_to

def index(request):
    if request.method == 'GET':
        form = InquiriesForm()
    else:
        form = InquiriesForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                name,
                message,
                email_to,
                [email],
                fail_silently=False
            )

            form.save()

    context = {
                'form' : form,
                'data' : Inquiries.objects.all()
            }

    return render(request, 'f_heart/index.html', context)
