from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView as BaseLogoutView
from django.utils.translation import gettext_lazy as _
from .forms import UserLoginForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


class IndexView(TemplateView):
    template_name = "index.html"


class LoginView(LoginView):
    authentication_form = UserLoginForm
    success_url = reverse_lazy("index")

    redirect_authenticated_user = True
    template_name = "general_form.html"

    def form_invalid(self, form) -> HttpResponse:
        messages.warning(
            self.request,
            _(
                "Please enter the correct username and password. "
                "Both fields can be case-sensitive."
            ),
        )
        return super().form_invalid(form)

    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, _("You are logged in"))
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["Title"] = _("Login")
        context["button"] = _("Login")
        return context


class LogoutView(BaseLogoutView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        super().post(request, *args, **kwargs)
        return redirect("/")
