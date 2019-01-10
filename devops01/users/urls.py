from django.conf.urls import url
from django.contrib import admin
from users import views
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/$',views.AuthView.as_view()),
    url(r'^api/v1/order/$',views.OrderView.as_view()),
]