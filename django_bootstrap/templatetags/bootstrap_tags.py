# -*- coding: utf-8 -*-
from django.forms.widgets import CheckboxInput
from django.template import Library
from django.utils.safestring import mark_safe


register = Library()


@register.inclusion_tag('bootstrap/form.html')
def bootstrap_form(form):
    return _show_form(form)


@register.inclusion_tag('bootstrap/wide_form.html')
def bootstrap_wide_form(form):
    return _show_form(form)


def _show_form(form):
    fields = []
    for field in form:
        field.is_checkbox = isinstance(field.field.widget, CheckboxInput)
        bits = field.label_tag().split('>', 1)
        field.label_attrs = mark_safe(bits[0].split(' ', 1)[-1])
        field.label_text = bits[1].split('<')[0]
        fields.append(field)
    return {
        'form': form,
        'fields': fields,
    }
