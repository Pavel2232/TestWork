from django.contrib import admin
from django.urls import path
from rest_framework import routers

from suppliers.views import SuppliersView

router = routers.SimpleRouter()
router.register('api', SuppliersView)

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls
