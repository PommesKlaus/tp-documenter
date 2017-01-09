from django import template
from django.utils import formats
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=False)
def date_or_infinite(value):
    """If value is None, use infinity-symbol, else format date as short date."""
    if value is None:
        return mark_safe('&#8734;')
    try:
        return formats.date_format(value, "SHORT_DATE_FORMAT")
    except AttributeError:
        try:
            return format(value, "SHORT_DATE_FORMAT")
        except AttributeError:
            return ''