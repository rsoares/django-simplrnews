# -*- coding: utf-8 -*-
# Ricardo Soares (ricardo@dengun.com) - Dengun 2011

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from photologue.models import ImageModel


class NewsArticle(models.Model):
    """Defines a new article."""
    title = models.CharField(_("Title"), max_length=50)
    url_slug = models.SlugField(max_length=255, db_index=True, unique=True)
    summary = models.CharField(_("Summary"), max_length=128)
    content = models.TextField(_("Content"))
    published = models.BooleanField(_("Publish"), default=False)
    on_homepage = models.BooleanField(_("Show on Homepage"), default=False)
    registration_date = models.DateTimeField(_("Created on"), auto_now_add=True)
    publication_date = models.DateTimeField(_("Published on"), null=True, blank=True)
    
    class Meta:
        ordering = ['title']
        db_table = 'news_article'
        verbose_name = _('News article')
        verbose_name_plural = _('News articles')

    def __unicode__(self):
        return self.title


class NewsPhoto(ImageModel):
    """ Provides custom functionality for images in articles. """

    POSITIONAL_CHOICES = (
        (0, _("Center")),
        (1, _("Left")),
        (2, _("Right"))
    )

    position = models.PositiveIntegerField(_("Position"), default=1, choices=POSITIONAL_CHOICES)
    article = models.ForeignKey('news.NewsArticle', verbose_name=_("Image"))

    class Meta:
        db_table = 'news_photos'
        verbose_name = _('News photo')
        verbose_name = _('News photos')


class NewsSubscriber(models.Model):
    """ Newsletter subscribers. """
    email = models.EmailField(unique=True)
    name = models.CharField(_("Name"), max_length=64, null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'news_subscriber'
        verbose_name = _('News subscriber')
        verbose_name_plural = _('News subscribers')

    def __unicode__(self):
        return self.email
    
