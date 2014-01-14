# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request, session, flash, render_template, redirect, url_for
from captcha.forms import DemoForm
from captcha.utilities.captcha import captcha


mod = Blueprint('views', __name__)


@mod.route('/', methods=['GET', 'POST'])
def index():
    form = DemoForm()

    if request.method == 'GET' or form.validate_on_submit() is False:
        captcha()
        captcha_path = session['captcha_path']

    if form.validate_on_submit():
        flash("Captcha passed!", 'success')
        return redirect(url_for('views.index'))

    if form.errors:
        flash("Danger", 'danger')

    return render_template('index.html',
        form=form,
        captcha_path=captcha_path)
