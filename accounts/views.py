from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

from accounts.forms import RegistrationForm

class CustomLoginView(LoginView):
    template_name = 'registration.html'
    
class CustomRegisterView(LoginView):
    template_name = 'registration.html'
    

def custom_logout(request):
    logout(request)
    return redirect('/')

def register(request):
    print(request)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                print("Authentication failed")
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
        
    return render(request, 'registration.html', {'form': form})