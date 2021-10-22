from django.db import models
from django.utils.translation import gettext_lazy as _


def default_class_hint():
    return {}


def default_attr_hint():
    return {
        'refer': '',
        'use_collection': None,
        'value_choices': [],
        'key_type': '',
        'value_type': '',
        'datetime_format': '%Y-%m-%d %H:%M:%S',
        'default_value': None,
    }


class AttrDataTypeChoices(models.TextChoices):
    INTEGER = 'INTEGER', _('Integer')
    FLOAT = 'FLOAT', _('Float')
    STRING = 'STRING', _('String')
    DATETIME = 'DATETIME', _('Datetime')
    BOOLEAN = 'BOOLEAN', _('Boolean')
    MAP = 'MAP', _('Map')
    LIST = 'LIST', _('List')


class Class(models.Model):
    name_human = models.CharField(_('Class name for human'), max_length=64)
    name = models.CharField(_('Class name'), max_length=64)
    hint = models.JSONField(_('Class hint'), default=default_class_hint, blank=True)
    time_added = models.DateTimeField(_('Time Added'), auto_now_add=True)
    time_updated = models.DateTimeField(_('Time Updated'), auto_now=True)

    def __str__(self):
        return f'{self.name_human}'


class Attr(models.Model):
    of_class: Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    name_human = models.CharField(_('Attr name for human'), max_length=64)
    name = models.CharField(_('Attr name'), max_length=64)
    dtype = models.CharField(_('Attr data type'),
                             max_length=64,
                             choices=AttrDataTypeChoices.choices,
                             default=AttrDataTypeChoices.STRING)
    hint = models.JSONField(_('Attr hint'), default=default_attr_hint, blank=True)
    time_added = models.DateTimeField(_('Time Added'), auto_now_add=True)
    time_updated = models.DateTimeField(_('Time Updated'), auto_now=True)

    def __str__(self):
        return self.fullname_human()

    def fullname(self):
        return f'{self.of_class.name}.{self.name}'

    def fullname_human(self):
        return f'{self.of_class.name_human}{self.name_human}'
