"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('',  name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include("blog.urls"))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from orders.views import stripe_webhook_view
from products.views import IndexView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("products/", include("products.urls", namespace="products")),
    path("users/", include("users.urls", namespace="users")),
    # OAuth
    path("accounts/", include("allauth.urls")),
    # orders
    path("orders/", include("orders.urls", namespace="orders")),
    path("webhook/stripe", stripe_webhook_view, name="stripe_webhook"),
    path("api/", include("api.urls", namespace="api")),
    path('api-token-auth/', obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
