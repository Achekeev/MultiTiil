from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('sign_up/', RegisterView.as_view(), name='sign up'),
    path('login/', TokenObtainPairView.as_view(), name='login-obtain-token'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login-refresh-token'),

]