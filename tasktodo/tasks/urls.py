from django.urls import path
from tasks.views import (
    TaskList, TaskDetail, TaskCheck, TaskUncheck, api_root
    )

urlpatterns = [
    path('api', api_root),
    
    path("api/tasks/",TaskList.as_view(),name=TaskList.name),
    path("api/tasks/<int:pk>",TaskDetail.as_view(),name=TaskDetail.name),
    path('api/tasks/<int:pk>/check/', TaskCheck.as_view(), name=TaskCheck.name),
    path('api/tasks/<int:pk>/uncheck/', TaskUncheck.as_view(), name=TaskUncheck.name),
    
]
