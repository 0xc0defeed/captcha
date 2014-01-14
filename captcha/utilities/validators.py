# -*- coding: utf-8 -*-
from flask import session
from wtforms.validators import ValidationError


class Captcha(object):
    """"""
    def __init__(self, message=None):

        if not message:
            message = u'Please try again.'

        self.message = message

    def __call__(self, form, field):

        captcha_number = session['captcha_number']

        if not field.data in captcha_number:
            raise ValidationError(self.message)
