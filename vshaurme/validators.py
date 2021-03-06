import os
import re
import requests

from flask import current_app
from flask_babel import _
from flask_babel import lazy_gettext as _l

from wtforms import ValidationError

from transliterate import translit


def is_bad_username(self, field):
    for word in read_swear_words():
        if word.strip() in field.data:
            raise ValidationError(_l("Please don't use swear words in username"))


def read_swear_words():
    path = current_app.config['SWEAR_WORDS']
    if os.path.getsize(path) > 0:
        with open(path, 'r') as f:
            swear_words = [line for line in f]
    return swear_words


def has_upper_letter(form, field):
    password = field.data
    pattern = r'[A-Z]'
    if not re.search(pattern, password):
        raise ValidationError(_('Password should contain at least 1 capital letter'))


def has_lower_letter(form, field):
    password = field.data
    pattern = r'[a-z]'
    if not re.search(pattern, password):
        raise ValidationError(_('Password should contain at least 1 lowercase letter'))


def has_digit(form, field):
    password = field.data
    pattern = r'\d'
    if not re.search(pattern, password):
        raise ValidationError(_('Password should contain at least 1 digit'))



def is_long_enought(form, field):
    min_lenght = 10
    message = _('Password should be not less then %d symbols') % (min_lenght)
    l = field.data and len(field.data) or 0
    if l < min_lenght:
        raise ValidationError(message)


password_validators = [has_upper_letter, has_lower_letter, has_digit, is_long_enought]