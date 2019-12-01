from django.db import models
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager

JOB_APPLY_TYPE_CHOICES = [
    ('clt', 'CLT'),
    ('pj', 'PJ'),
    ('others', _('Others')),
]

REMOTE_TYPE_CHOICES = [
    ('full_remote', _('100% Remote')),
    ('partial_remote', _('Partial Remote')),
    ('onsite', _('On-Site')),
]


class Job(models.Model):
    title = models.CharField(_('Title'), max_length=200, db_index=True)
    description = models.TextField(_('Description'), )
    location = models.CharField(_('Location'), max_length=200)
    apply_type = models.CharField(_('Apply Type'), max_length=200, choices=JOB_APPLY_TYPE_CHOICES, default='clt')
    how_to_apply = models.TextField(_('How to Apply'), null=True, blank=True)
    requirements = models.TextField(_('Requirements'), )
    remote_type = models.CharField(_('Remote Type'), max_length=200, choices=REMOTE_TYPE_CHOICES, default='onsite')
    active = models.BooleanField(_('Active'), default=True)
    tags = TaggableManager()
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta: 
       ordering = ('-updated_at', ) 
       verbose_name = _("Job")
       verbose_name_plural = _("Jobs")

    def __str__(self):
        return self.title