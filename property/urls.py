from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()

router.register('list', views.PropertyViewset)
router.register('propertyType', views.PropertyTypeViewset)
router.register('purpose', views.PurposeViewset)
router.register('reviews', views.ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]