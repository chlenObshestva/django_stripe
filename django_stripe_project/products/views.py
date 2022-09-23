import stripe
from django.views.generic import TemplateView
from django.conf import settings
from django.views import View
from django.conf import settings
from django.shortcuts import redirect
from .models import Product
from django.views.decorators.csrf import csrf_exempt


stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductLandingPageView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        product_id = self.kwargs['pk']
        product = Product.objects.get(id=product_id)
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        product = Product.objects.get(id=product_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                        'name': product.name,
                        },
                        'unit_amount': product.price,
                    },
                    'quantity': 1,
                }],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url, code=303)

