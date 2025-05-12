from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Label
from django.utils.translation import gettext_lazy as _
from .forms import LabelForm
from task_manager.mixins import (
    CustomLoginRequiredMixin,
    ContextMixin,
    ContextDeleteMixin,
)


class LabelListView(CustomLoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/index.html"
    context_object_name = "labels"


class LabelCreateView(CustomLoginRequiredMixin, ContextMixin, CreateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy("label_list")
    text = _("Create label")
    button = _("Create")
    success_message = _("Label created successfully")


class LabelUpdateView(CustomLoginRequiredMixin, ContextMixin, UpdateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy("label_list")
    text = _("Update label")
    button = _("Update")
    success_message = _("Label updated successfully")


class LabelDeleteView(
    CustomLoginRequiredMixin,
    ContextDeleteMixin,
    DeleteView
):
    model = Label
    success_url = reverse_lazy("label_list")
    text = _("Delete label")
    sucess_delete_message = _("Label deleted successfully")
