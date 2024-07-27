from . import views
from django.urls import path
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("drinks/", views.drinklist, name = "drink_list"),
    path("drinks/<int:id>", views.drink_detail),
    path("api/schema", SpectacularAPIView.as_view(), name = "schema"),
    path("api/schema/docs", SpectacularSwaggerView.as_view(url_name = "schema")),
]
