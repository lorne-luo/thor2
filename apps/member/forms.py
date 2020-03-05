from django import forms
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm, PasswordResetForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from core.auth_user.models import AuthUser


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
        model = AuthUser
        fields = ['password1', 'password2']

    def save(self, commit=True, request=None,
             email_template_name='email/admin_reset_password_txt.html',
             html_email_template_name='email/admin_reset_password.html',
             from_email=None):

        self.set_password(self.cleaned_data['new_password1'])

        # print self.email_user
        if self.cleaned_data['new_password1'] and self.cleaned_data['email_user'] and self.username:
            from django.template import loader
            from django.contrib.sites.models import get_current_site
            from django.core.mail import EmailMultiAlternatives

            current_site = get_current_site(request)
            if not from_email:
                from_email = settings.DEFAULT_FROM_EMAIL

            c = {
                'name': self.get_name(),
                'username': self.username,
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
        model = AuthUser
        fields = ['password1', 'password2']


class RegisterForm(forms.Form):
    mobile = forms.CharField(label="澳洲或国内手机", error_messages={'required': _('澳洲或国内手机号, 必填项')}, validators=[
        RegexValidator(regex='^\d*$', message='澳洲或国内手机号，无需区号', code='Invalid number')])
    password = forms.CharField(widget=forms.PasswordInput, label="密 码", min_length=6, error_messages={
        'min_length': _('密码最小长度6位'),
        'required': _('密码, 必填项'),
    })
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="确认密码", min_length=6, error_messages={
        'min_length': _('密码最小长度6位'),
        'required': _('重复密码, 必填项'),
    })

    def clean(self):
        mobile = self.cleaned_data.get('mobile')
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_confirm')

        if password1 and password1 != password2:
            self.add_error('password_confirm', '确认密码不匹配，请重新输入')
        if AuthUser.objects.filter(mobile=mobile).exists():
            self.add_error('mobile', '该手机号码已存在')

        return self.cleaned_data


class LoginForm(forms.Form):
    mobile = forms.CharField(label="澳洲或国内手机或电子邮件", error_messages={'required': _('请填写手机号或电子邮件')})
    password = forms.CharField(widget=forms.PasswordInput, label="密 码", min_length=6, error_messages={
        'min_length': _('密码最小长度6位'),
        'required': _('请填写密码'),
    })


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, error_messages={'required': _('请填写电子邮件')})

    def clean_email(self):
        email = self.cleaned_data['email']
        if not AuthUser.objects.filter(email=email).exists():
            raise forms.ValidationError("该电子邮件不存在，请重新输入")
        return email


class CustomSetPasswordForm(SetPasswordForm):
    error_messages = {
        'password_mismatch': _("确认密码不匹配，请重新输入"),
    }
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="密 码", min_length=6, error_messages={
        'min_length': _('密码最小长度6位'),
        'required': _('密码, 必填项'),
    })
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="确认密码", min_length=6, error_messages={
        'min_length': _('密码最小长度6位'),
        'required': _('重复密码, 必填项'),
    })
