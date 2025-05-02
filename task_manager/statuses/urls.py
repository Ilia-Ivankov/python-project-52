from django.urls import path
from task_manager.statuses import views

urlpatterns = [
    path("", views.StatusesIndexView.as_view(), name="statuses_index"),
    path("create/", views.StatusesCreateView.as_view(), name="status_create"),
    path(
        "<int:pk>/update/",
        views.StatusesUpdateView.as_view(),
        name="status_update"),
]
