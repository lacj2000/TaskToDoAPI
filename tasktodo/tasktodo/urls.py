from django.contrib import admin
from django.urls import path, include, re_path

# Swagger
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
   
   path('admin/', admin.site.urls),
    
   re_path(r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('',include('users.urls')),
   path('',include('tasks.urls')),
]

 
 
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
