from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ClientList

router = DefaultRouter(trailing_slash=False)
router.register('clients', ClientList, 'clients')

app_name = 'api'

urlpatterns = router.urls

urlpatterns += [
]