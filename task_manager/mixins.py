from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.db import models


class CustomLoginRequiredMixin(LoginRequiredMixin):
    permission_denied_message = _("You are not logged in! Please log in")
    login_url = reverse_lazy("login")
    redirect_field_name = None

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()


class UserOwnershipMixin(UserPassesTestMixin):
    permission_message = _("You do not have permission to perform this action")

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                _("You are not logged in! Please log in"))
            return redirect(reverse_lazy("login"))

        messages.error(self.request, self.permission_message)
        return redirect(self.success_url)


class UserEditPermissionMixin(UserOwnershipMixin):
    permission_message = _("You do not have permission to edit this user.")

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        user = self.get_object()
        return self.request.user == user


class UserDeletePermissionMixin(UserOwnershipMixin):
    permission_message = _("You do not have permission to delete this user.")

    def test_func(self):
        user = self.get_object()
        if not self.request.user.is_authenticated:
            return False
        return self.request.user == user

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                _("You are not logged in! Please log in"))
            return redirect(reverse_lazy("login"))
        else:
            messages.error(self.request, self.permission_message)
        return redirect(self.success_url)


class ContextDeleteMixin:
    template_name = "general_delete_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["text"] = self.text
        context["delete_warning"] = self.get_delete_warning()
        return context

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.sucess(request, self.sucess_delete_message)
            return response
        except models.ProtectedError as e:
            messages.error(request, e.args[0])
            return redirect(self.success_url)

    def get_delete_warning(self):
        return (
            _("Are you sure you want to delete")
            + " "
            + self.get_object().name
            + "?"
        )


class FormValidMixin:
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.error_message:
            messages.error(self.request, self.error_message)
            return super().form_invalid(form)
        return super().form_invalid(form)


class ContextMixin(FormValidMixin):
    template_name = "general_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["text"] = self.text
        context["button"] = self.button
        return context
