from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    info=openapi.Info(
        title="TASTE OF ASIA",
        default_version='v1',
        description='this is food order restaurant project',
        terms_of_service='http://www.google.com/policies/terms/',
        contact=openapi.Contact(email='kedeikulkyzy.medina@gmail.com'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    re_path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/accounts/', include('user.urls')),
    path('api/v1/foods/', include('food.urls')),
    path('api/v1/foods/categories/', include('category.urls')),
    path('api/v1/foods/comments/', include('commentary.urls')),

    # path('api/v1/rest-auth/', include('rest_auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
