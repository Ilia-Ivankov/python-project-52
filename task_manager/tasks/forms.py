from django import forms
import django_filters
from task_manager.labels.models import Label
from .models import Task
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status

User = get_user_model()


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Name"),
        widget=forms.TextInput(attrs={"placeholder": _("Name")})
    )
    description = forms.CharField(
        label=_("Description"),
        widget=forms.Textarea(attrs={"placeholder": _("Description")})
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label=_("Status"),
        widget=forms.Select(attrs={
            "class": "form-select",
            "id": "id_status",
            "data-testid": "id_status",
            "aria-label": _("Status")
        })
    )
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label=_("Executor"),
        widget=forms.Select(attrs={
            "class": "form-select",
            "id": "id_executor",
            "data-testid": "id_executor",
            "aria-label": _("Executor"),
            "name": "executor"
        })
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_("Labels"),
        required=False,
        widget=forms.SelectMultiple(attrs={
            "class": "form-select",
            "id": "id_labels",
            "data-testid": "id_labels",
            "aria-label": _("Labels")
        })
    )

    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]


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
