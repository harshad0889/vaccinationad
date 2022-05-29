from datetime import datetime, timedelta
import threading
import time

from vaxin.wsgi import *
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.vaxin")

from kids.views import automsg


class BackgroundTasks(threading.Thread):
    def run(self, *args, **kwargs):


        # updated = (datetime.now() +
        #            timedelta(minutes=1)).strftime('%H:%M:%S')
        #
        # # print("Current Time =", current_time)
        # print(updated)
        # while True:
        #     d = datetime.now()
        #     current_time = d.strftime("%H:%M:%S")
        #     print(current_time)
        #     if (updated == current_time):
        while True:
            automsg()
            time.sleep(1)


t = BackgroundTasks()
t.start()
