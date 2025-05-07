from django import forms
import django_filters
from task_manager.labels.models import Label
from .models import Task
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status

User = get_user_model()


class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()


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
        label=_("Status"),
        queryset=Status.objects.all(),
        empty_label=None,
        widget=forms.Select()
    )
    executor = UserModelChoiceField(
        queryset=User.objects.all(),
        label=_("Executor"),
        empty_label=None,
        widget=forms.Select()
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_("Labels"),
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
