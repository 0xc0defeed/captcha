# -*- coding: utf-8 -*-
from flask import session
from config import STATIC_FOLDER
import random
from datetime import datetime, timedelta
from PIL import Image
import os
from os import path


def captcha():

    infilePath = os.path.join(STATIC_FOLDER, "img/captcha/input/")
    outfilePath = os.path.join(STATIC_FOLDER, "img/captcha/output/")
    numbers = random.sample(xrange(10), 6)
    outfileName = ('%06x' % random.randrange(16 ** 16))
    extension = '.jpg'
    now = datetime.now() - timedelta(minutes=1)

    layer0 = Image.open(infilePath + str(numbers[0]) + extension)
    layer1 = Image.open(infilePath + str(numbers[1]) + extension)
    layer2 = Image.open(infilePath + str(numbers[2]) + extension)
    layer3 = Image.open(infilePath + str(numbers[3]) + extension)
    layer4 = Image.open(infilePath + str(numbers[4]) + extension)
    layer5 = Image.open(infilePath + str(numbers[5]) + extension)

    image = Image.new("RGB", (48, 15))

    image.paste(layer0, (0, 0))
    image.paste(layer1, (8, 0))
    image.paste(layer2, (16, 0))
    image.paste(layer3, (24, 0))
    image.paste(layer4, (32, 0))
    image.paste(layer5, (40, 0))

    image.save(outfilePath + outfileName + extension)

    for filename in os.listdir(outfilePath):
        filetime = datetime.fromtimestamp(path.getctime(outfilePath + filename))

        if filetime < now:
            os.remove(os.path.join(outfilePath, filename))

    captchaNumber = (''.join(str(x) for x in numbers))
    captchaPath = outfileName + extension

    session['captcha_number'] = captchaNumber
    session['captcha_path'] = captchaPath
