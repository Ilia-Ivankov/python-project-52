from typing import Any
from django.db import models


class StatusDeletionError(Exception):
    pass


class Status(models.Model):
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def delete(
        self, using: Any = ..., keep_parents: bool = ...
    ) -> tuple[int, dict[str, int]]:
        if self.task_set.exists():
            raise StatusDeletionError("Can't delete status because it's in use")
        return super().delete(using, keep_parents)
