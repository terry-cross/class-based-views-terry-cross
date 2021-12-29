from django.conf.urls import url
from django.urls import path
from home import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name = 'homepage'),
    path('other/', other, name = 'otherpage'),
    path('about/', about, name = 'aboutpage'),
    path('model_form_upload/', model_form_upload, name = 'model_form_upload'),
    path('simple_upload/', simple_upload, name = 'simple_upload'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)