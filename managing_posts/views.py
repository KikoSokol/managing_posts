from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

SCHEMA_VIEW = get_schema_view(
    openapi.Info(
        title="Managing posts",
        default_version='v1',
        description="AMCEF - test assignment",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)