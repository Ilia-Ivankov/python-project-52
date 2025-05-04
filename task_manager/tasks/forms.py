from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]
        labels = {
            "name": _("Name"),
            "description": _("Description"),
            "status": _("Status"),
            "executor": _("Executor"),
            "labels": _("Labels"),
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": _("Name")}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": _("Description")}
            ),
            "status": forms.Select(
                attrs={"class": "form-select", "placeholder": _("Status")}
            ),
            "executor": forms.Select(
                attrs={"class": "form-select", "placeholder": _("Executor")}
            ),
            "labels": forms.SelectMultiple(
                attrs={"class": "form-select", "placeholder": _("Labels")}
            ),
        }
