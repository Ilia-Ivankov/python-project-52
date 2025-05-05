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
from task_manager.mixins import CustomLoginRequiredMixin, FormContextMixin
from django_filters.views import FilterView
from .forms import TaskFilter


class TaskListView(CustomLoginRequiredMixin, FilterView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    filterset_class = TaskFilter


class TaskCreateView(FormContextMixin, CustomLoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "general_form.html"
    success_url = reverse_lazy("tasks_index")
    text = "Create task"
    button = "Create"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskUpdateView(FormContextMixin, CustomLoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "general_form.html"
    success_url = reverse_lazy("tasks_index")
    text = "Update task"
    button = "Update"

    def form_valid(self, form):
        messages.success(self.request, _("Task successfully updated"))
        return super().form_valid(form)


class TaskDeleteView(CustomLoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = "general_delete_form.html"
    success_url = reverse_lazy("tasks_index")

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_action"] = self.request.path
        context["text"] = _("Delete task")
        context["delete_warning"] = (
            _("Are you sure you want to delete")
            + " "
            + self.get_object().name + "?"
        )
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(request, _("Task successfully deleted"))
        return super().delete(request, *args, **kwargs)


class TaskDetailView(CustomLoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.get_object().id
        context["labels"] = self.get_object().labels.all()
        context["status"] = self.get_object().status
        context["owner"] = self.get_object().owner
        context["executor"] = self.get_object().executor
        context["created_at"] = self.get_object().created_at
        context["description"] = self.get_object().description
        return context
