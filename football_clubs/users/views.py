from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from users.forms import UserForm


class LoginUser(LoginView):
    form_class = UserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизація'}

    # def get_success_url(self):
    #     return reverse_lazy('main')


# class LogoutUser(LogoutView):
#     template_name = 'users/logout.html'
#
#     def get_success_url(self):
#         return reverse_lazy('main')

# def login_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             clean = form.cleaned_data
#             user = authenticate(request, username=clean['username'], password=clean['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('main'))
#     else:
#         form = UserForm()
#     return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
