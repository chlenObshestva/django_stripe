from django.contrib import admin
from django.urls import path
from products.views import (
    CreateCheckoutSessionView,
    ProductLandingPageView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<pk>/', ProductLandingPageView.as_view(), name='landing-page'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]
