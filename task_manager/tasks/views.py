from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Task
from .forms import TaskForm
from task_manager.mixins import (
    CustomLoginRequiredMixin,
    ContextMixin,
    ContextDeleteMixin,
)
from django_filters.views import FilterView
from .forms import TaskFilter


class TaskListView(CustomLoginRequiredMixin, FilterView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    filterset_class = TaskFilter


class TaskCreateView(CustomLoginRequiredMixin, ContextMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks_index")
    text = _("Create task")
    button = _("Create")
    success_message = _("Task created successfully")


class TaskUpdateView(CustomLoginRequiredMixin, ContextMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks_index")
    text = _("Update task")
    button = _("Update")
    success_message = _("Task updated successfully")


class TaskDeleteView(
    CustomLoginRequiredMixin,
    UserPassesTestMixin,
    ContextDeleteMixin,
    DeleteView
):
    model = Task
    template_name = "general_delete_form.html"
    success_url = reverse_lazy("tasks_index")
    text = _("Delete task")
    sucess_delete_message = _("Task successfully deleted")

    def test_func(self):
        return self.request.user == self.get_object().owner

    def handle_no_permission(self):
        if not self.test_func():
            messages.error(
                self.request,
                _("A task can only be deleted by its author."))
            return redirect(self.success_url)
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()


class TaskDetailView(CustomLoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = self.get_object()
        return context
