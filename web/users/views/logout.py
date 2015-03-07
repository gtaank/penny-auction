from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from pennyauction.libs.views import BaseView


class LogoutView(BaseView):
    def get(self):
        if self.request.user.is_authenticated():
            logout(self.request)
        return redirect(reverse('dashboard_page'))


def logout_page(request):
    return LogoutView(request=request).respond_with()
