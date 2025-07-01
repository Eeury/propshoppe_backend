from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse  

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/', include('payments.urls')),

    
    path('', lambda request: JsonResponse({
        "message": "✅ Backend is live!",
        "status": "ok"
    })),
]
