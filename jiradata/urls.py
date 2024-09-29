from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JIRAViewSet, ExternalApiViewSet, MyModelViewSet, IssueTypeData

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'fields', JIRAViewSet)
router.register(r'external-api', ExternalApiViewSet, basename='external-api')
router.register(r'mymodel', MyModelViewSet, basename='mymodel')
router.register(r'issuetypes', IssueTypeData, basename='issuetype')


# Include the router's URLs in your app's urlpatterns
urlpatterns = [
    path('fields/', include(router.urls)),
]