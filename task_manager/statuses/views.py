from typing import Any
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Status
from .forms import StatusForm


class StatusesIndexView(LoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/index.html"
    context_object_name = "statuses"
    permission_denied_message = _("You are not logged in! Please log in")
    login_url = reverse_lazy("login")

    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()


class StatusesCreateView(LoginRequiredMixin, CreateView):
    model = Status
    template_name = "general_form.html"
    success_url = reverse_lazy("statuses_index")
    form_class = StatusForm
    permission_denied_message = _("You are not logged in! Please log in")
    login_url = reverse_lazy("login")

    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, _("The status was created successfully"))
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["button"] = _("Create")
        context["text"] = _("Create status")
        return context

    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()


class StatusesUpdateView(LoginRequiredMixin, UpdateView):
    form_class = StatusForm
    model = Status
    template_name = "general_form.html"
    success_url = reverse_lazy("statuses_index")
    permission_denied_message = _("You are not logged in! Please log in")
    login_url = reverse_lazy("login")

    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, _("The status was updated successfully"))
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["button"] = _("Update")
        context["text"] = _("Update status")
        return context

    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()
