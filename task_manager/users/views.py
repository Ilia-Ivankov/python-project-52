from django.contrib import messages
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserRegisterForm
from django.db import models
from task_manager.mixins import (
    CustomLoginRequiredMixin,
    UserEditPermissionMixin,
    UserDeletePermissionMixin,
)


class UsersIndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, "users/index.html", context={"users": users})


class UsersCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "general_form.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form) -> HttpResponse:
        messages.success(
            self.request,
            _("The user has been successfully registered"))
        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["title"] = _("Registration")
        context["button"] = _("Register")
        return context


class UsersUpdateView(
    CustomLoginRequiredMixin,
    UserEditPermissionMixin,
    UpdateView
):
    model = User
    form_class = UserRegisterForm
    template_name = "general_form.html"
    success_url = reverse_lazy("users")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["title"] = _("Changing the user")
        context["button"] = _("Change")
        return context

    def form_valid(self, form):
        messages.success(self.request, _("User successfully edited"))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            _(
                "There was an error with your submission. "
                "Please correct the errors below."
            ),
        )
        return super().form_invalid(form)


class UserDeleteView(
    CustomLoginRequiredMixin,
    UserDeletePermissionMixin,
    DeleteView
):
    model = User
    template_name = "general_delete_form.html"
    success_url = reverse_lazy("users")

    def post(self, request: HttpRequest, *args: str, **kwargs: Any):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(request, _("User successfully deleted"))
            return response
        except models.ProtectedError as e:
            messages.error(request, e.args[0])
            return redirect(self.success_url)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["form_action"] = self.request.path
        context["text"] = _("Deleting user")
        context["delete_warning"] = (
            _("Are you sure you want to delete") + " " + user.username + "?"
        )
        return context
