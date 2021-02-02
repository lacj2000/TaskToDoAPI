
from django.urls import path

from users.views import UserList, UserDetail

urlpatterns = [
    path('api/users/', UserList.as_view(), name=UserList.name),
    path('api/users/<int:pk>', UserDetail.as_view(), name=UserDetail.name),
]
