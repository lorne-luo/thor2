import os

from django.db import models
from django.core.mail import send_mail
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, Group, Permission
from django.db.models import Q
from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils.http import urlquote
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.contrib.auth.hashers import is_password_usable, make_password
from settings.settings import BASE_DIR, ID_PHOTO_FOLDER
#
# def modify_fields(**kwargs):
#     def wrap(cls):
#         for field, prop_dict in kwargs.items():
#             for prop, val in prop_dict.items():
#                 setattr(cls._meta.get_field(field), prop, val)
#         return cls
#
#     return wrap
#
#
# @modify_fields(groups={'verbose_name': _('customer groups'),
#                        'related_name': "customer_set",
#                        'related_query_name': "customer"})


class InterestTag(models.Model):
    name = models.CharField(_(u'name'), max_length=30, null=False, blank=False)
    remarks = models.CharField(verbose_name='remarks', max_length=500, null=True, blank=True)
    # tags = models.ManyToManyField(Customer, verbose_name=_('mobile number'), null=True, blank=True)

    class Meta:
        verbose_name_plural = _('InterestTags')
        verbose_name = _('InterestTag')

    def __unicode__(self):
        return '[T]%s' % self.name


class Customer(AbstractBaseUser):
    name = models.CharField(_(u'name'), max_length=30, null=False, blank=False)
    email = models.EmailField(_('email address'), max_length=254, null=True, unique=True, blank=True)
    mobile = models.CharField(_('mobile number'), max_length=15, null=True, blank=True,
                              validators=[validators.RegexValidator(r'^[\d-]+$', _('plz input validated mobile number'), 'invalid')])

    primary_address = models.ForeignKey('Address', blank=True, null=True, verbose_name=_('primary address'), related_name=_('primary address'))

    tags = models.ManyToManyField(InterestTag, verbose_name=_('Tags'), null=True, blank=True)
    groups = models.ManyToManyField(Group, verbose_name=_('customer groups'),
                                    blank=True, help_text=_('The groups this user belongs to. A customer will '
                                                            'get all permissions granted to each of '
                                                            'his/her group.'),
                                    related_name="customer_set", related_query_name="customer")
    user_permissions = models.ManyToManyField(Permission,
                                              verbose_name=_('customer permissions'), blank=True,
                                              help_text=_('Specific permissions for this customer.'),
                                              related_name="customer_set", related_query_name="customer")
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True, null=True)

    objects = UserManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name_plural = _('Customer')
        verbose_name = _('Customer')
        permissions = (

        )

    # def __init__(self, *args, **kwargs):
    #     super(Customer, self).__init__(*args, **kwargs)
    #     # snip the other fields for the sake of brevity
    #     # Adding content to the form
    #     self.fields['groups'].verbose_name = 'customer groups'

    def __unicode__(self):
        return '[C]%s' % self.name

    def get_full_name(self):
        return self.name.strip()

    def get_short_name(self):
        return self.name.strip()

    def clean(self):
        if not is_password_usable(self.password):
            self.password = make_password(self.password)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # Note: this is not called on bulk operations
        self.clean()
        super(Customer, self).save(force_insert, force_update, using, update_fields)

    def get_token(self):
        '''
         Get user's token for authentification via rest-api. Creates new if
         does not exist yet.
        '''
        token, _created = Token.objects.get_or_create(user=self)
        return token

    def renew_token(self):
        ''' Delete token and create a new one (since token is PK) '''
        token, created = Token.objects.get_or_create(user=self)

        if not created:
            token.delete()
            token, _created = Token.objects.get_or_create(user=self)

        return token

    def is_member(self, group_name):
        return self.groups.filter(name=group_name).exists()

    def get_absolute_url(self):
        return "/customer/%s" % urlquote(self.email)

    def email_user(self, subject, message, from_email=None):
        if self.email:
            send_mail(subject, message, from_email, [self.email])

    def generate_password(self):
        '''
        Regenerate a password
        '''
        self.password = get_random_string(8, 'abcdefghjklmnpqrstuvwxyz0123456789')


@receiver(pre_save, sender=Customer)
def create_password(sender, instance=None, created=False, **kwargs):
    if not instance.id:
        instance.generate_password()


def get_id_photo_front_path(instance, filename):
    ext = filename.split('.')[-1]
    count = Address.objects.filter(customer=instance.customer).count()
    filename = '%s_%s_front.%s' % (instance.customer.id, count, ext)
    path = os.path.join(BASE_DIR, ID_PHOTO_FOLDER, filename)
    return path


def get_id_photo_back_path(instance, filename):
    ext = filename.split('.')[-1]
    count = Address.objects.filter(customer=instance.customer).count()
    filename = '%s_%s_back.%s' % (instance.customer.id, count, ext)
    path = os.path.join(BASE_DIR, ID_PHOTO_FOLDER, filename)
    return path


class Address(models.Model):
    name = models.CharField(_(u'name'), max_length=30, null=False, blank=False)
    mobile = models.CharField(_('mobile number'), max_length=15, null=True, blank=True,
                              validators=[validators.RegexValidator(r'^[\d-]+$', _('plz input validated mobile number'), 'invalid')])
    address = models.CharField(verbose_name='address', max_length=50, null=False, blank=False)
    customer = models.ForeignKey(Customer, blank=False, null=False, verbose_name='customer')
    id_photo_front = models.FileField(upload_to=get_id_photo_front_path, blank=True, null=True, verbose_name=_('ID Front'))
    id_photo_back = models.FileField(upload_to=get_id_photo_back_path, blank=True, null=True, verbose_name=_('ID Back'))

    class Meta:
        verbose_name_plural = _('Address')
        verbose_name = _('Address')

    def __unicode__(self):
        return '[A]%s,%s,%s' % (self.name, self.mobile, self.address)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        addr_set = Address.objects.filter(customer=self.customer)
        count = addr_set.count()
        super(Address, self).save(force_insert, force_update, using, update_fields)

        if not count:
            super(Address, self).save(force_insert, force_update, using, update_fields)
            self.customer.primary_address = self
            self.customer.save()

    def id_photo_link(self):

        return self.id_photo_front_link() + self.id_photo_back_link()

    id_photo_link.allow_tags = True
    id_photo_link.short_description = 'ID_photo'

    def id_photo_front_link(self):
        if self.id_photo_front:
            file_path = str(self.id_photo_front)
            base, file_path = file_path.split('/%s' % ID_PHOTO_FOLDER)
            url = '/%s%s' % (ID_PHOTO_FOLDER, file_path)
            return '<a target="_blank" href="%s"><img width="90px" src="%s"></a>' % (url, url)
        else:
            return ''

    id_photo_front_link.allow_tags = True
    id_photo_front_link.short_description = 'ID_photo_front'

    def id_photo_back_link(self):
        if self.id_photo_back:
            file_path = str(self.id_photo_back)
            base, file_path = file_path.split('/%s' % ID_PHOTO_FOLDER)
            url = '/%s%s' % (ID_PHOTO_FOLDER, file_path)
            return '<a target="_blank" href="%s"><img width="90px" src="%s"></a>' % (url, url)
        else:
            return ''

    id_photo_back_link.allow_tags = True
    id_photo_back_link.short_description = 'ID_photo_back'
