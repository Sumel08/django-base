from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('ping', views.PingViewSet, base_name='ping')

urlpatterns = [
    url(r'', include(router.urls))
]
