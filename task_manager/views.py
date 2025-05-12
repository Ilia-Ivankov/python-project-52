from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView as BaseLogoutView
from django.utils.translation import gettext_lazy as _
from .forms import UserLoginForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .mixins import ContextMixin, FormValidMixin


class IndexView(TemplateView):
    template_name = "index.html"


class LoginView(ContextMixin, FormValidMixin, LoginView):
    authentication_form = UserLoginForm
    success_url = reverse_lazy("index")
    text = _("Login")
    button = _("Log in")
    redirect_authenticated_user = True
    template_name = "general_form.html"
    success_message = _("You are logged in")
    error_message = _(
        "Please enter the correct username and password. "
        "Both fields can be case-sensitive."
    )


class LogoutView(BaseLogoutView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        super().post(request, *args, **kwargs)
        return redirect("/")
