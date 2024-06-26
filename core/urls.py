from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('products/<int:pk>', views.products_list, name='products'),
    path('products/add', views.add_product, name='add_product'),
    path('products/delete/<int:pk>', views.delete_product, name='delete_product'),
    path('products/purchase/<int:pk>', views.purchase_product, name='purchase_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)