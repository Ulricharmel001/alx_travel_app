# project urls
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

# ---------------------------------
# Swagger setup
# ---------------------------------
schema_view = get_schema_view(
    openapi.Info(
        title="Teh-Dewah Blog API",
        default_version='v1',
        description="API documentation for Teh-Dewah Blog",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# ---------------------------------
# URL Patterns
# ---------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication endpoints
    path('api/auth/', include('accounts.urls')),

    # Blog endpoints
    path('api/blog/', include('teh_blog_api.urls')),

    # Swagger UI endpoint
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]