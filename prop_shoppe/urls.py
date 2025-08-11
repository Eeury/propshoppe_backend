from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
       path('grappelli/', include('grappelli.urls')), 
       path('admin/', admin.site.urls),
       path('api/token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
       path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
       path('api/', include('products.urls')),
       path('api/', include('orders.urls')),
       path('api/', include('chat.urls')),
       path('api/signup/', include('accounts.urls')),
       path('ckeditor/', include('ckeditor_uploader.urls')),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)