"""
This is a test app for running cron job
"""
from django.core.mail import send_mail

from django_cron import CronJobBase, Schedule

class CronJob(CronJobBase):
    """
    This is a sample class that will execute the job every N number of minutes. This
    uses the django_cron app to perform

    To execute run "python manage.py runcrons "name_of_cron_job"

    For our need, we will use Azure's WebJob to execute the above every 5 minutes. So
    as a developer we need to tell that WebJob the name of the cronjobs to execute

    The name of the cronjob will also need to be added to base.py setting file, under
    CRON_CLASSES session.

    Documentation available here: http://django-cron.readthedocs.org/en/latest/
    """
    RUN_EVERY_MINS = 3

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'util.cron.CronJob'    # a unique code

    def do(self):
        """
        Test email send for cron job
        """
        send_mail('Subject here',
                  'Here is the message.',
                  'superuser@admin.net',
                  ['superuser@admin.net'],
                  fail_silently=False)
