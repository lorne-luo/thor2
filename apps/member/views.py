# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, resolve_url
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import TemplateView, FormView

from core.auth_user.models import AuthUser
from .forms import RegisterForm, LoginForm

log = logging.getLogger(__name__)


@sensitive_post_parameters()
@csrf_exempt
@ensure_csrf_cookie
@never_cache
def member_login(request):
    if request.method == 'GET':
        c = csrf(request)
        if request.GET.get('next'):
            c.update({'next': request.GET['next']})
        c.update({'form': LoginForm()})
        return render_to_response('adminlte/login.html', c)
    elif request.method == 'POST':
        old_user = request.user or None
        form = LoginForm(request.POST)
        if not form.is_valid():
            form.data = {'mobile': form.data.get('mobile')}
            return render_to_response('adminlte/login.html', {'form': form})

        # old_schema=connection.schema_name
        # connection.set_schema_to_public()

        mobile = form.cleaned_data.get('mobile')
        password = form.cleaned_data.get('password')
        user = authenticate(username=mobile, password=password)
        if user:
            login(request, user)
            next_page = request.POST.get('next', None)
            # If the user was already logged-in before we ignore the ?next
            # parameter, this avoids a loop of login prompts when the user does
            # not have the permission to see the page in ?next
            if old_user == user or not next_page:
                # Redirect chefs to meals page
                next_page = resolve_url(settings.LOGIN_REDIRECT_URL)

            # connection.set_schema(old_schema)
            return HttpResponseRedirect(next_page)
        else:
            form.add_error(None, '密码错误，请重试')
            form.data = {'mobile': mobile}
            # connection.set_schema(old_schema)
            return render_to_response('adminlte/login.html', {'form': form})


def member_home(request):
    return HttpResponse('123')


def member_logout(request):
    connection.set_schema_to_public()
    logout(request)
    return redirect('member-login')


class AgentView(TemplateView):
    template_name = 'member/agent.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class RegisterView(FormView):
    template_name = 'adminlte/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('member-login')

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        mobile = form.cleaned_data.get('mobile')
        password = form.cleaned_data.get('password')
        AuthUser.objects.create_staff(mobile, None, password, premium_account=False)
        messages.success(self.request, '注册成功, 请登陆.')

        return super(RegisterView, self).form_valid(form)
