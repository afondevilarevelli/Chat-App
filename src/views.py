from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from src.forms import UserLoginForm, UserSignUpForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class UserLoginView(FormView):
    template_name = 'src/index.html'
    form_class = UserLoginForm
    success_url = 'chats/'

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)

        messages.error(self.request, _('Invalid credentials'))
        return self.form_invalid()

class UserCreateView(FormView):
    template_name = 'src/sign_up.html'
    form_class = UserSignUpForm
    success_url = 'chats/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        messages.success(self.request, _('User created succesfully!'))
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

@login_required
def chat(req, room_name):
    return render(req, 'src/chats.html', {'room_name': room_name})