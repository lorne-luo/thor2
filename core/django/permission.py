# coding=utf-8
import inspect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models


class ProfileRequiredMixin(LoginRequiredMixin):
    profile_required = []

    def check_perm(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return False

        profile_class_name = '%s.%s' % (request.profile._meta.app_label, request.profile._meta.model_name)
        for profile in self.profile_required:
            if isinstance(profile, str) and profile.lower() == profile_class_name:
                return True
            elif inspect.isclass(profile) and issubclass(profile, models.Model) and isinstance(request.profile,
                                                                                               profile):
                return True
        return False

    def dispatch(self, request, *args, **kwargs):
        if self.check_perm(request, *args, **kwargs):
            return super(ProfileRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()


class CustomerRequiredMixin(ProfileRequiredMixin):
    profile_required = ('customer.customer',)
