# celery config file
import os
from celery import Celery

# point celery to django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

# create celery app
app = Celery('alx_travel_app')

# load celery settings from django settings (CELERY_ prefix)
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto load tasks from all apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    return 'Debug task executed'

if __name__ == '__main__':
    app.start()
