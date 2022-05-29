import os
import threading
import time

import django
from vaxin.wsgi import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.vaxin")

from kids.views import automsg
from django.conf import settings


class BackgroundTasks(threading.Thread):
    def run(self, *args, **kwargs):
        while True:
            automsg()
            time.sleep(1)


t = BackgroundTasks()
t.start()
