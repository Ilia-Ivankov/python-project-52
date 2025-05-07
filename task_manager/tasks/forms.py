from django import forms
import django_filters
from task_manager.labels.models import Label
from .models import Task
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status

User = get_user_model()


class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label=_("Status")
    )
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label=_("Executor")
    )

    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]
        labels = {
            "name": _("Name"),
            "description": _("Description"),
            "labels": _("Labels"),
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": _("Name")}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": _("Description")}
            ),
            "labels": forms.SelectMultiple(),
        }


class TaskFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Labels'),
        required=False)
    self_tasks = django_filters.BooleanFilter(
        field_name='owner',
        method='filter_self_tasks',
        label=_('Only my tasks'),
        widget=forms.CheckboxInput,
    )

    class Meta:
        model = Task
        fields = ["status", "executor", "labels", "self_tasks"]

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(owner=self.request.user)
        return queryset
