from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('qoutes', views.QuoteViewset, basename='qoutes')
urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.UserAPIView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetailAPIView.as_view(), name='user-detail'),
]
