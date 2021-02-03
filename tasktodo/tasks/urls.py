from django.urls import path
from tasks.views import TaskList, TaskDetail

urlpatterns = [
    path("api/tasks/",TaskList.as_view(),name=TaskList.name),
    path("api/tasks/<int:id>",TaskDetail.as_view(),name=TaskDetail.name),
]
