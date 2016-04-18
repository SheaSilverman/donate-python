from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import StripeForm

from django.http import HttpResponse

import json
import stripe

class StripeMixin(object):
    def get_context_data(self, **kwargs):
        context = super(StripeMixin, self).get_context_data(**kwargs)
        context['publishable_key'] = settings.STRIPE_PUBLIC_KEY
        return context


class SuccessView(TemplateView):
    template_name = 'thank_you.html'


class DonateView(StripeMixin, FormView):
    success_url = reverse_lazy('thank_you')
    form_class = StripeForm

    def form_valid(self, form):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
          charge = stripe.Charge.create(
                amount=form.cleaned_data['amount'],
                currency="usd",
                source=form.cleaned_data['stripe_token'], # obtained with Stripe.js
                description="Shea Silverman Campaign Donation",
                metadata= {
                            "occupation": form.cleaned_data['occupation'],
                            "employer": form.cleaned_data['employer'],
                        }
          )
        except stripe.error.CardError:
          # The card has been declined
          pass

        return super(DonateView, self).form_valid(form)

