# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import Required, Email
from captcha.utilities.validators import Captcha


class DemoForm(Form):
    email = TextField(validators=[Required(), Email()])
    captcha = TextField(validators=[Required(), Captcha()])
    submit = SubmitField()
