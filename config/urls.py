"""config re_path Configuration

The `re_pathpatterns` list routes re_paths to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/re_paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a re_path to re_pathpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a re_path to re_pathpatterns:  path('', Home.as_view(), name='home')
Including another re_pathconf
    1. Import the include() function: from django.re_paths import include, path
    2. Add a re_path to re_pathpatterns:  path('blog/', include('blog.re_paths'))
"""
# from django.contrib import admin
# from django.re_paths import path, include, re_path
# from rest_framework.permissions import AllowAny
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from django.conf import settings
# from django.conf.re_paths.static import static


# schema_re_path_patterns = [ path('', include('hashtag.re_paths')), ] 

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#       patterns=schema_re_path_patterns,
#    ),
#    validators=['flex', 'ssv'],
#    public=True,
#    permission_classes=(AllowAny,),
# )

# re_pathpatterns =( [
#     re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
#     path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
#     path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

#     path('admin/', admin.site.re_paths),
#     re_path(r'^', include('hashtag.re_paths')),
#     ]
#     + static(settings.MEDIA_re_path, document_root=settings.MEDIA_ROOT)
#     + static(settings.STATIC_re_path, document_root=settings.STATIC_ROOT)
# )

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 


schema_view = get_schema_view(
   openapi.Info(
      title="42MARU API",
      default_version='v1',
      description="42마루 기업프로젝트 API",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hashtag.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]