# -*- coding: utf-8 -*-
import os


_basedir = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(_basedir, 'captcha/static')


DEBUG = True


#: python2 -c "print repr(__import__('os').urandom(24))"
SECRET_KEY = '\xe1\xb7\xa6\x03\xefN\x0e>\xda\xd5gQ2\x97+Ap\x05\xba\xd3\xf72\r\t'


CSRF_ENABLED = True
#: ('%06x' % random.randrange(16**32))
CSRF_SESSION_KEY = '6f321702d69d4e5d16a5f79ab4bd24dd'
