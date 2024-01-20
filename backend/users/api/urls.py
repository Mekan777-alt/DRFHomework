from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.api.views.change_password import reset_password, change_password
from users.api.views.registration import register
from users.api.views.user import UserViewSet

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend([
    path('auth/registration', register),
    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/reset-password/', reset_password, name='reset-password'),
    path('me', UserViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update'
    })),
    path('auth/change-password', change_password, name='change-password')
])
