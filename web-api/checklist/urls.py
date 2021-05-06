from django.urls import path
from .views import ListTasksView, CreateTaskView


urlpatterns = [
    path('list/', ListTasksView.as_view()),
    path('create/', CreateTaskView.as_view()),
]
