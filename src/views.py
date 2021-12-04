from django.shortcuts import redirect, render
from src.forms import ChatForm
from django.views.generic.edit import FormView

class UserFormView(FormView):
    template_name = 'src/index.html'
    form_class = ChatForm
    success_url = 'chat/'

    def form_valid(self, form):
        return redirect(self.get_success_url() + form.cleaned_data['name'])

def chat(req, room_name):
    return render(req, 'src/chat.html', {'room_name': room_name})