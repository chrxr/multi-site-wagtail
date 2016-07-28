from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page, Orderable, Site
from wagtail.wagtailcore.fields import RichTextField, StreamField

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel,)

class HomePage(Page):
    body = models.CharField(max_length=255, null=True, blank=True)
