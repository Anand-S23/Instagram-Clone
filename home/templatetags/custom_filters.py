from __future__ import unicode_literals
import datetime
from django import template
from django.utils.html import avoid_wrapping
from django.utils.timezone import is_aware, utc
from django.utils.translation import ugettext, ungettext_lazy

register = template.Library()
TIMESINCE_CHUNKS = (
    (60 * 60 * 24 * 365, ungettext_lazy('%d year', '%d years')),
    (60 * 60 * 24 * 30, ungettext_lazy('%d month', '%d months')),
)
@register.filter
def yearssince(d, now=None):
    # Convert datetime.date to datetime.datetime for comparison.
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)
    if now and not isinstance(now, datetime.datetime):
        now = datetime.datetime(now.year, now.month, now.day)

    if not now:
        now = datetime.datetime.now(utc if is_aware(d) else None)

    delta = now - d
    # ignore microseconds
    since = delta.days * 24 * 60 * 60 + delta.seconds
    if since <= 0:
        # d is in the future compared to now, stop processing.
        return avoid_wrapping(ugettext('0 minutes'))
    for i, (seconds, name) in enumerate(TIMESINCE_CHUNKS):
        count = since // seconds
        if count != 0:
            break
    result = avoid_wrapping(name % count)

    return result