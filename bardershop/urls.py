from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import (
    ServicesByMasterView,
    MainView,
    ThanksTemplateView,
    ReviewCreateView,
    ReviewThanksTemplateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cabinet/', include('users.urls', namespace='users')),
    path("", MainView.as_view(), name='main'),
    path("thanks/", ThanksTemplateView.as_view(), name='thanks'),
    path(
        'get_services_by_master/<int:master_id>/',
        ServicesByMasterView.as_view(),
        name='get_services_by_master',
    ),
    path("review/create/", ReviewCreateView.as_view(), name="review_create"),
    path("review/thanks/", ReviewThanksTemplateView.as_view(), name="review_thanks"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
