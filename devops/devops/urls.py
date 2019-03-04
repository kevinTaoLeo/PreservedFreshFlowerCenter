"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework.routers import  DefaultRouter
from idcs.views import IdcViewset
from users.views import UserViewset
from cabinet.views import CabinetViewset
from rest_framework.documentation import include_docs_urls

route = DefaultRouter()
route.register("idcs", IdcViewset, base_name="idcs")
route.register("users", UserViewset, base_name="users")
route.register("cabinet", CabinetViewset, base_name="cabinet")
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
urlpatterns = [
    url(r'^',include(route.urls)),
    url(r'^docs/', schema_view, name="docs"),
    url(r'^docss/',include_docs_urls("永生花运维平台接口文档"))
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^idcs/',include("idcs.urls")),
# ]
