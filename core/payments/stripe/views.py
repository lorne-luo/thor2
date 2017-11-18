import stripe
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView, TemplateView
from django.views.generic.base import TemplateResponseMixin, ContextMixin
from django.views.generic.edit import ProcessFormView
from djstripe.models import Card

from core.payments.stripe.stripe_api import STRIPE_PUBLIC_KEY


class PaymentsContextMixin(object):
    """Adds checkout context to a view."""

    def get_context_data(self, **kwargs):
        """Inject STRIPE_PUBLIC_KEY and plans into context_data."""
        context = super(PaymentsContextMixin, self).get_context_data(**kwargs)
        context.update({
            "STRIPE_PUBLIC_KEY": STRIPE_PUBLIC_KEY,
        })

        return context


class UpdateCreditCardView(LoginRequiredMixin, PaymentsContextMixin, TemplateView):
    """A view to render the add card template."""
    template_name = "djstripe/add_card.html"

    def post(self, request, *args, **kwargs):
        token = request.POST.get("cardToken", None)

        if token is None:
            messages.error(self.request, 'Some errors happened, please retry.')
            raise Http404

        try:
            profile = self.request.user.profile
            card = profile.add_card(source=token)  # input card token or detail dict
        except stripe.error.CardError as ex:
            context = self.get_context_data(**kwargs)
            context.update({'error': ex._message})
            return self.render_to_response(context)

        messages.success(self.request, 'Your credit card updated.')
        return HttpResponseRedirect(reverse_lazy('payments:add_card'))



class RemoveAllCardView(LoginRequiredMixin, RedirectView):
    http_method_names = ['post']
    pattern_name = 'payments:add_card'

    def post(self, request, *args, **kwargs):
        profile = self.request.user.profile
        profile.remove_all_card()
        return super(RemoveAllCardView, self).post(request, *args, **kwargs)


class RemoveSingleCardView(LoginRequiredMixin, RedirectView):
    http_method_names = ['post']
    pattern_name = 'payments:add_card'

    def post(self, request, *args, **kwargs):
        card_id = kwargs.get("pk")
        card = Card.objects.filter(id=card_id).first()
        if card:
            profile = self.request.user.profile
            profile.remove_card(card.stripe_id)
        return super(RemoveSingleCardView, self).post(request, *args, **kwargs)
