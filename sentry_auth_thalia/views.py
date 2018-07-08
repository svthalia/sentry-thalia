#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

from django.core.exceptions import NON_FIELD_ERRORS
from django import forms
from sentry.auth.view import AuthView, ConfigureView
from sentry.models import AuthIdentity

from .client import ThaliaClient, ThaliaApiError

class UserAuthForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    did_submit = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    provider = forms.CharField(widget=forms.HiddenInput, initial='thalia')

    def __init__(self, *args, **kwargs):
        super(UserAuthForm, self).__init__(*args, **kwargs)


class UserAuthView(AuthView):
    def __init__(self, *args, **kwargs):
        self.client = ThaliaClient()
        super(UserAuthView, self).__init__(*args, **kwargs)

    def handle(self, request, helper):
        params = None
        if request.POST.get('did_submit'):
            params = request.POST
        form = UserAuthForm(params)
        if form.is_valid():
            try:
                token_data = self.client.authenticate(form.cleaned_data['username'], form.cleaned_data['password'])
                helper.bind_state('auth_token', token_data.get('token'))
                user_data = self.client.get_user(token_data.get('token'))
                helper.bind_state('user', user_data)
                return helper.next_step()
            except ThaliaApiError as e:
                if e.status >= 300:
                    if 'detail' in e.message:
                        form._errors[NON_FIELD_ERRORS] = [e.message['detail']]
                    else:
                        for key in e.message:
                            field = NON_FIELD_ERRORS if key == 'non_field_errors' else key
                            form._errors[field] = form.error_class(e.message.get(key))
                            if field in form.cleaned_data:
                                    del form.cleaned_data[field]
                else:
                    form._errors[NON_FIELD_ERRORS] = ['Something went wrong with the API request: {}'.format(e.message)]
            

        return self.respond('sentry_auth_thalia/user-auth.html', {
            'form': form,
        })


class ThaliaConfigureView(ConfigureView):
    def dispatch(self, request, *args, **kwargs):
        return self.render('sentry_auth_thalia/configure.html')
