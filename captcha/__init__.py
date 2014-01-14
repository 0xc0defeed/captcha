# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)
app.config.from_object('config')


from captcha.views import mod as viewsModule
app.register_blueprint(viewsModule)
