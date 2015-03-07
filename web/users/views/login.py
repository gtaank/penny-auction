from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

from pennyauction.libs.views import BaseView
from web.users.forms.login import LoginForm


class LoginView(BaseView):
    template_name = 'users/login.html'

    def get(self):
        form = LoginForm()
        return {'form': form}

    def post(self):
        form = LoginForm(self.request.POST)
        if not form.is_valid():
            return self.get_context_data(form=form)

        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user and user.is_active:
            login(self.request, user)
            return redirect("dashboard_page")
        else:
            form.errors['email'] = ['Email not in system']
            return self.get_context_data(form=form)


def login_view(request):
    return LoginView(request=request).respond_with()