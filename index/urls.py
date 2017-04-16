from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
from index.views import UserViewSet
from index.views import GroupViewSet
from views import DjangoUsers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^test/(\d+)/$', DjangoUsers),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
