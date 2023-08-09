from django.shortcuts import render
from authentication.forms import UserRegistrationForm

# Create your views here.
def home(request):
    register_form = UserRegistrationForm(request.POST)
    return render(request, 'home.html', {'register_form': register_form})