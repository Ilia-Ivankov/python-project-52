from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import User
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name="tasks")
    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='tasks_owned'
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='tasks_executed'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
