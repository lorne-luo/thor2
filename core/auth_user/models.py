from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager

from core.auth_user.constant import ADMIN_GROUP


class AuthUserManager(UserManager):
    def _create_user(self, password, is_staff, is_superuser, mobile=None, email=None, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not mobile and not email:
            raise ValueError('Mobile and email must give one')
        email = self.normalize_email(email)
        user = self.model(username=mobile or email, email=email, mobile=mobile, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile=None, email=None, password=None, **extra_fields):
        return self._create_user(password, False, False, mobile, email, **extra_fields)

    def create_superuser(self, mobile, email, password, **extra_fields):
        return self._create_user(password, True, True, mobile=mobile, email=email, **extra_fields)

    def identify(self, mobile_or_email):
        if '@' in mobile_or_email:
            return super(AuthUserManager, self).get(email=mobile_or_email)
        else:
            return super(AuthUserManager, self).get(mobile=mobile_or_email)


class AuthUser(AbstractUser):
    mobile = models.CharField(_('mobile'), max_length=30, unique=True, blank=True)

    objects = AuthUserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'mobile'

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        unique_together = ('email',)

    @property
    def profile(self):
        if getattr(self, 'seller', None):
            return getattr(self, 'seller')
        elif getattr(self, 'customer', None):
            return getattr(self, 'customer')
        return None

    @property
    def is_seller(self):
        return getattr(self, 'seller') is not None

    @property
    def is_customer(self):
        return getattr(self, 'customer') is not None

    def __str__(self):
        return '%s' % self.get_username()

    def get_username(self):
        return self.mobile or self.email

    def in_group(self, group_names):
        if not isinstance(group_names, (list, tuple)):
            group_names = (group_names,)

        if self.is_superuser:
            return True
        user_groups = self.groups.values_list("name", flat=True)
        intersection = set(group_names).intersection(set(user_groups))
        return bool(intersection)


class UserProfileMixin(object):
    @property
    def profile(self):
        return self

    @property
    def username(self):
        return self.auth_user.get_username()

    @property
    def date_joined(self):
        return self.auth_user.date_joined

    @property
    def is_admin(self):
        return self.auth_user.is_superuser or self.in_group(ADMIN_GROUP)

    @property
    def is_active(self):
        return self.auth_user.is_active

    def in_group(self, group_names):
        return self.auth_user.in_group(group_names)
