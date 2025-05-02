from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import UserRegisterForm


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
            _("The user has been successfully registered")
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["title"] = _("Registration")
        context["button"] = _("Register")
        return context


class UsersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserRegisterForm
    template_name = "general_form.html"
    success_url = reverse_lazy("users")

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                _("You are not logged in! Please log in."))
            return redirect(reverse_lazy("login"))
        messages.error(
            self.request,
            _("You do not have permission to edit this user.")
        )
        return redirect(self.success_url)

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


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = "general_delete_form.html"
    success_url = reverse_lazy("users")

    def test_func(self):
        user = self.get_object()
        if not self.request.user.is_authenticated:
            return False
        if self.request.user == user:
            return True
        return False

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                _("You are not logged in! Please log in."))
            return redirect(reverse_lazy("login"))
        if self.request.user != self.get_object():
            messages.error(
                self.request,
                _("You do not have permission to delete this user.")
            )
            return redirect(reverse_lazy("users"))
        return super().handle_no_permission()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["form_action"] = self.request.path
        context["text"] = _("Deleting user")
        context["delete_warning"] = (
            _("Are you sure you want to delete ") + user.username
        )
        return context
