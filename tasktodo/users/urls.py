
from django.urls import path, re_path

from users.views import UserList, UserDetail

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="TaskToDo API",
      default_version='v2',
      description="API ToDo List",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="luizjuniordeveloper@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    

    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
 
    path('users/', UserList.as_view(), name=UserList.name),
    path('users/<int:pk>/', UserDetail.as_view(), name=UserDetail.name),



]
 
 
 
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),