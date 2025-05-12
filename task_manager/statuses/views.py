from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Status
from .forms import StatusForm
from task_manager.mixins import (
    CustomLoginRequiredMixin,
    ContextMixin,
    ContextDeleteMixin,
)


class StatusesIndexView(CustomLoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/index.html"
    context_object_name = "statuses"


class StatusesCreateView(CustomLoginRequiredMixin, ContextMixin, CreateView):
    model = Status
    success_url = reverse_lazy("statuses_index")
    form_class = StatusForm
    success_message = _("The status was created successfully")


class StatusesUpdateView(CustomLoginRequiredMixin, ContextMixin, UpdateView):
    form_class = StatusForm
    model = Status
    success_url = reverse_lazy("statuses_index")
    text = _("Update status")
    button = _("Update")
    success_message = _("The status was updated successfully")


class StatusesDeleteView(
    CustomLoginRequiredMixin,
    ContextDeleteMixin,
    DeleteView
):
    model = Status
    template_name = "general_delete_form.html"
    success_url = reverse_lazy("statuses_index")
    text = _("Delete status")
    success_delete_message = _("The status was deleted successfully")
