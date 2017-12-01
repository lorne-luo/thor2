from dal import autocomplete
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q, Count, Case, IntegerField, When
from apps.express.models import ExpressCarrier, ExpressOrder


class ExpressCarrierAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    paginate_by = 50

    def get_queryset(self):
        # order by carrier usage
        qs = ExpressCarrier.objects.order_by_usage(self.request.user)

        if self.q:
            qs = qs.filter(Q(name_cn__icontains=self.q))
        if self.q.isalpha():
            qs = qs.filter(pinyin__contains=self.q.lower())
        return qs
