from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

ARTICLE_STATUS_CHOICES = [
    ('draft', _('Draft')),
    ('publish', _('Publish')),
    ('schedule', _('Schedule')),
    ('trash', _('Trash')),
]


class Article(models.Model):

    title = models.CharField(_('Title'), max_length=250, db_index=True)
    slug = models.SlugField(_('Slug'), max_length=200, unique=True)
    content = models.TextField(_('Content'), )
    short_content = models.CharField(_('Short Content'), max_length=250, blank=True)
    status = models.CharField(_('Status'), max_length=100, default='draft', choices=ARTICLE_STATUS_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    published_at = models.DateTimeField(_('Published At'), auto_now_add=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta: 
       ordering = ('-published_at', ) 
       verbose_name = _("Article")
       verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title
