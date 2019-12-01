from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class JobsConfig(AppConfig):
    name = 'jobs'
    verbose_name = _('Jobs')
