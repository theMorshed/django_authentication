from django.shortcuts import render
from authentication.forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():        
            register_form.save()
            messages.success(request, 'Account created successfully')
            # print(register_form.cleaned_data)
    else:
        register_form = UserRegistrationForm()

    return render(request, 'home.html', {'register_form': register_form})