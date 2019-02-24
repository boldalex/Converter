from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_converter.settings')

app = Celery('online_converter')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

#app.conf.beat_schedule = {
    #'update_db_rates': {
    #     'task': 'converter.tasks.update_rates_from_api',
     #    'schedule': timedelta(seconds=60 * 60)
    #}
#}