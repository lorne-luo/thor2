''' Source: https://djangosnippets.org/snippets/2275/ '''
from django import template
from django.utils import timezone
from django.utils.translation import ugettext, ungettext

register = template.Library()


@register.filter
def humanize_timesince(date):
    now = timezone.localtime(timezone.now())
    if date > now:
        return date.strftime('%d/%m/%Y') # in the future

    delta = now - date

    num_years = delta.days / 365
    if num_years > 0:
        return ungettext("%d year ago", "%d years ago", num_years) % num_years

    num_weeks = delta.days / 7
    if num_weeks > 0:
        return ungettext("%d week ago", "%d weeks ago", num_weeks) % num_weeks

    if delta.days > 0:
        return ungettext("%d day ago", "%d days ago", delta.days) % delta.days

    num_hours = delta.seconds / 3600
    if num_hours > 0:
        return ungettext("%d hour ago", "%d hours ago", num_hours) % num_hours

    num_minutes = delta.seconds / 60
    if num_minutes > 0:
        return ungettext("%d minute ago", "%d minutes ago", num_minutes) % num_minutes

    return ugettext("just a few seconds ago")
