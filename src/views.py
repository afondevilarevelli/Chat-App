from django.shortcuts import redirect, render
from src.forms import UserForm
from django.views.generic.edit import FormView

class UserFormView(FormView):
    template_name = 'src/index.html'
    form_class = UserForm
    success_url = 'chat'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)

def chat(req):
    return render(req, 'src/chat.html')