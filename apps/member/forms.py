'''
Copyright (c) 2013 O7 Technologies Pty Ltd trading as Omniscreen. All Rights Reserved.

O7 Technologies Pty Ltd trading as Omniscreen ("Omniscreen") retains copyright
on all text, source and binary code contained in this software and documentation.
Omniscreen grants Licensee a limited license to use this software,
provided that this copyright notice and license appear on all copies of the software.
The software source code is provided for reference, compilation and porting purposes only
and may not be copied, modified or distributed in any manner and by any means
without prior written permission from Omniscreen.

THIS SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS,"
WITHOUT ANY WARRANTY OF ANY KIND. ALL EXPRESS OR IMPLIED CONDITIONS,
REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT, ARE HEREBY EXCLUDED.
OMNISCREEN SHALL NOT BE LIABLE FOR ANY DAMAGES SUFFERED BY LICENSEE
AS A RESULT OF USING OR MODIFYING THE SOFTWARE OR ITS DERIVATIVES.

IN NO EVENT WILL OMNISCREEN BE LIABLE FOR ANY LOST REVENUE, PROFIT OR DATA,
OR FOR DIRECT, INDIRECT, SPECIAL, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES,
HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY,
ARISING OUT OF THE USE OF OR INABILITY TO USE SOFTWARE,
EVEN IF OMNISCREEN HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
'''
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm
from .models import Seller


class SellerProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        if 'username_readonly' in kwargs:
            username_readonly = kwargs.pop('username_readonly')
        else:
            username_readonly = False

        super(SellerProfileForm, self).__init__(*args, **kwargs)
        if username_readonly:
            self.fields['username'].widget.attrs['readonly'] = True

    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Seller
        fields = ['username', 'name', 'email',
                  'is_active', 'groups', 'mobile', 'password']


class PasswordLengthValidator(object):
    ''' check password length '''

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < 4:
            raise ValidationError("Password must be at least 4 characters.")
        return password1


class ResetPasswordEmailForm(SetPasswordForm, PasswordLengthValidator):
    email_user = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'toggle'}))

    class Meta:
        model = Seller
        fields = ['password1', 'password2']

    def save(self, commit=True, request=None,
             email_template_name='email/admin_reset_password_txt.html',
             html_email_template_name='email/admin_reset_password.html',
             from_email=None):

        self.user.set_password(self.cleaned_data['new_password1'])

        # print self.email_user
        if self.cleaned_data['new_password1'] and self.cleaned_data['email_user'] and self.user.email:
            from django.template import loader
            from django.contrib.sites.models import get_current_site
            from django.core.mail import EmailMultiAlternatives

            current_site = get_current_site(request)
            if not from_email:
                from_email = settings.DEFAULT_FROM_EMAIL

            c = {
                'name': self.user.get_short_name(),
                'username': self.user.username,
                'password': self.cleaned_data['new_password1'],
                'site_name': current_site.name,
                'site': current_site.domain
            }

            subject = 'Password Reset'
            email = loader.render_to_string(email_template_name, c)

            if html_email_template_name:
                html_email = loader.render_to_string(html_email_template_name, c)
            else:
                html_email = None

            msg = EmailMultiAlternatives(subject, email, from_email, [self.user.email])
            msg.attach_alternative(html_email, "text/html")
            msg.send()

        if commit:
            self.user.save()
        return self.user


class UserResetPasswordForm(PasswordChangeForm, PasswordLengthValidator):
    class Meta:
        model = Seller
        fields = ['password1', 'password2']
