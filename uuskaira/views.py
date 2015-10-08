# encoding: utf-8

import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_GET
from django.views.generic.base import TemplateView


@require_GET
def logout_view(request):
    logout(request)
    next_url = request.GET.get('next', settings.LOGOUT_REDIRECT_URL)
    return redirect(next_url)


class UuskairaView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(UuskairaView, self).get_context_data(**kwargs)
        context.update(
            kompassi=settings.KOMPASSI_HOST,
        )
        return context
