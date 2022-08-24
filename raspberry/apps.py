from django.apps import AppConfig
from .views import index
import requests
import sched
import time
import threading
from datetime import datetime
def repeat_at_interval(scheduler, event, interval=60, add_n=10, start_t=None):
    """Adds 'add_n' more calls to "event" at each "interval" seconds"""
    # Unix timestamp
    if start_t is None:
        t = time.time()
        # round to next interval -
        t = t - (t % interval) + interval
    else:
        t = start_t

    for i in range(add_n):
        scheduler.enterabs(t, 0, event)
        t += interval

    # Schedule call to self, to add "add_n" extra events
    # when these are over:
    scheduler.enterabs(t - interval, 0, repeat_at_interval, kwargs={
        "scheduler": scheduler,
        "event": event,
        "interval": interval,
        "add_n": add_n,
        "start_t": t
        })


def test():
    print (datetime.now())

class RaspberryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'raspberry'

    def ready(self):
        scheduler = sched.scheduler(time.time, time.sleep)
        repeat_at_interval(scheduler, test, interval=60)
        thread = threading.Thread(target=scheduler.run)
        thread.start()
        while True:
            time.sleep(10)
            urlMachine = 'http://localhost:8000/machines/2/'

            req = requests.get(urlMachine).json()

            if req['status'] == True:
                print('ENERGIZA')

            else:
                print('DESLIGA')
