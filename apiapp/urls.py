from django.urls import path, include
from rest_framework import routers
from .views import ListWork, RegisterView, LoginView
from django.contrib.auth.views import LogoutView

router = routers.SimpleRouter()
router.register(r'works',ListWork,basename="works")
# router.register(r'works/artist/', UserAddUpdateDelete, basename="users")
# router.register(r'works/type/', ReportingOfficers, basename="reportsto")


urlpatterns = [
   
    path('api/register/',RegisterView.as_view(),name='register'),
    path('api/login/',LoginView.as_view(),name='login'),
    path('api/logout/',LogoutView.as_view(),name='logout'),
    path('api/', include(router.urls)),
]