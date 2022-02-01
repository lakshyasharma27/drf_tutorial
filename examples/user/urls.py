from user import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# urlpatterns = [
#     path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
#     path('register', views.register, name='register'),
#     path('login', views.login, name='login'),
#     path('get_data', views.get_data, name='get_data'),    
# ]

urlpatterns = [
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),    
]
