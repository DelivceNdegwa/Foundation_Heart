from django.shortcuts import render, HttpResponse
from .forms import InquiriesForm, MembersOfProgramForm
from .models import Inquiries, MembersOfProgram

def index(request):

    if request.method == 'GET':
        form = InquiriesForm()
    else:
        form = InquiriesForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            form.save()

        else:
            return HttpResponse('Invalid details. Please Try again')
    context = {
        'form' : form,
        'data' : Inquiries.objects.all()
    }
    return render(request, 'f_heart/index.html', context)
