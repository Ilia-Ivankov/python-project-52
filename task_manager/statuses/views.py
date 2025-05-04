from typing import Any
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Status
from .forms import StatusForm
from django.db import models
from task_manager.mixins import CustomLoginRequiredMixin
from django.http import HttpResponse

class StatusesIndexView(CustomLoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/index.html"
    context_object_name = "statuses"


class StatusesCreateView(CustomLoginRequiredMixin, CreateView):
    model = Status
    template_name = "general_form.html"
    success_url = reverse_lazy("statuses_index")
    form_class = StatusForm

    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, _("The status was created successfully"))
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["button"] = _("Create")
        context["text"] = _("Create status")
        return context


class StatusesUpdateView(CustomLoginRequiredMixin, UpdateView):
    form_class = StatusForm
    model = Status
    template_name = "general_form.html"
    success_url = reverse_lazy("statuses_index")

    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, _("The status was updated successfully"))
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["button"] = _("Update")
        context["text"] = _("Update status")
        return context


class StatusesDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Status
    template_name = "general_delete_form.html"
    success_url = reverse_lazy("statuses_index")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["text"] = _("Delete status")
        context["delete_warning"] = _("Are you sure you want to delete") + self.get_object().name + "?"        
        return context

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(request, _("Status successfully deleted"))
            return response
        except models.ProtectedError as e:
            messages.error(request, e.args[0])
            return redirect(self.success_url)
