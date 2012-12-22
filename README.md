django-bootstrap
================

Install
```
pip install -e git+git://github.com/sdfsdhgjkbmnmxc/django-bootstrap.git#egg=djbootstrap
```

Setup settings.py
```python 
INSTALLED_APPS = (
    # ....
    'djbootstrap',
)
```

Usage:
```html
{% extends "djbootstrap/base.html" %}
{% load djbootstrap %}

{% block title %}my page{% endblock %}

{% block extrahead %}
    {{ block.super }}
{% endlbock %}

{% block body %}
    {{ block.super }}
    <form>
        bootstrap-like form:
        {% show_form form %}
        {# or {% show_wide_form form %} #}
    </form>
{% endblock %}
```