from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Label
from django.utils.translation import gettext_lazy as _
from .forms import LabelForm
from task_manager.mixins import CustomLoginRequiredMixin, FormContextMixin
from django.contrib import messages
from django.db import models
from django.shortcuts import redirect


class LabelListView(CustomLoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/index.html"
    context_object_name = "labels"


class LabelCreateView(FormContextMixin, CustomLoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = "general_form.html"
    success_url = reverse_lazy("label_list")
    text = "Create label"
    button = "Create"

    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, _("Label created successfully"))
        return super().form_valid(form)


class LabelUpdateView(FormContextMixin, CustomLoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = "general_form.html"
    success_url = reverse_lazy("label_list")
    text = "Update label"
    button = "Update"

    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, _("Label updated successfully"))
        return super().form_valid(form)


class LabelDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Label
    template_name = "general_delete_form.html"
    success_url = reverse_lazy("label_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["text"] = _("Delete label")
        context["delete_warning"] = _(
            "Are you sure you want"
            " to delete this label?")
        return context

    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(request, _("Label deleted successfully"))
            return response
        except models.ProtectedError as e:
            messages.error(request, e.args[0])
            return redirect(self.success_url)
