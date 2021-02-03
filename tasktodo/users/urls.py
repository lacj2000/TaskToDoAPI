
from django.urls import path, re_path

from users.views import UserList, UserDetail

# JWT
from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
   TokenVerifyView,
)


urlpatterns = [
    
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),



   path('api/users/', UserList.as_view(), name=UserList.name),
   path('api/users/<int:pk>/', UserDetail.as_view(), name=UserDetail.name),



]
 
