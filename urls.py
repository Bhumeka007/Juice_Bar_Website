from django.urls import path
from . import views
from .views import home, submit_feedback, add_to_cart

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('submit-feedback/', submit_feedback, name='submit_feedback'),
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('register/', views.register, name='register'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
