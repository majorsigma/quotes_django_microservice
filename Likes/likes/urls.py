from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('quotes', views.QuoteViewSet, basename='qoutes')
router.register('quoteusers', views.QuoteUserViewSet, basename='quoteusers')

urlpatterns = [
    path('', include(router.urls)),
    path('quotes/<int:pk>/like/', views.like, name='like'),
]
