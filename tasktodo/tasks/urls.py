from django.urls import path
from tasks.views import (
    TaskList, TaskDetail, TaskCheck, TaskUncheck, api_root, 
    SublistList, SublistDetail
    )

urlpatterns = [
    path('api', api_root),
    
    path("api/tasks/",TaskList.as_view(),name=TaskList.name),
    path("api/tasks/<int:pk>",TaskDetail.as_view(),name=TaskDetail.name),
    path('api/tasks/<int:pk>/check/', TaskCheck.as_view(), name=TaskCheck.name),
    path('api/tasks/<int:pk>/uncheck/', TaskUncheck.as_view(), name=TaskUncheck.name),
    path('api/tasks/<int:pk>/sublists/add/', SublistList.as_view(), name=SublistList.name),
    path('api/sublists/<int:pk>/', SublistDetail.as_view(), name=SublistDetail.name),
    
    


]
