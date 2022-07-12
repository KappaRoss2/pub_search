from celery.schedules import crontab

from .parser import find_copy as fc
from .parser import find_preprint as fp
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pub_search.settings')

app = Celery('pub_search')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'parse-articles-every-30-minute': {
        'task': 'main.tasks.find_copy_async',
        'task1': 'main.tasks.find_preprint_async',
        'schedule': crontab(minute=30),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}


@app.task
def find_copy_async(doi):
    driver = fc.init_session()
    copy = fc.find_copy(driver, doi)
    return copy


@app.task
def find_preprint_async(doi):
    driver = fp.init_session()
    preprint = fp.find_preprint(driver, doi)
    return preprint