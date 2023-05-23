from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Rejestracja nowego uzytkownika"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('creative_design1:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

def user_logout(request):
    return redirect(request, 'registration/user_logout.html')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('creative_design1/index.html')

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'registration/user_logout.html')