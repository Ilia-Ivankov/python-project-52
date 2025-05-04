from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect


class CustomLoginRequiredMixin(LoginRequiredMixin):
    permission_denied_message = _("You are not logged in! Please log in")
    login_url = reverse_lazy("login")
    redirect_field_name = None

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()


class UserOwnershipMixin(UserPassesTestMixin):
    permission_message = _("You do not have permission to perform this action")

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, _("You are not logged in! Please log in."))
            return redirect(reverse_lazy("login"))

        messages.error(self.request, self.permission_message)
        return redirect(self.success_url)


class UserEditPermissionMixin(UserOwnershipMixin):
    permission_message = _("You do not have permission to edit this user.")

    def test_func(self):
        user = self.get_object()
        return self.request.user == user


class UserDeletePermissionMixin(UserOwnershipMixin):
    permission_message = _("You do not have permission to delete this user.")

    def test_func(self):
        user = self.get_object()
        if not self.request.user.is_authenticated:
            return False
        return self.request.user == user
