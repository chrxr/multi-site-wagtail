from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page, Orderable

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel, PageChooserPanel, MultiFieldPanel)

from wagtail.contrib.settings.models import BaseSetting, register_setting

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

# The LinkFields and RelatedLink meta-models are taken from the WagtailDemo implementation.
# They provide a multi-field panel that allows you to set a link title and choose either
# an internal or external link. It also provides a custom property ('link') to simplify
# using it in the template.

class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
    ]

    class Meta:
        abstract = True

class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True

# The SocialMediaSettings model provides site-specific social media links.
# These could be easily expanded to include any number of social media URLs / IDs.

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL',
        null=True,
        blank=True
    )
    twitter = models.CharField(
        max_length=255,
        help_text='Your Twitter username, without the @',
        null=True,
        blank=True
    )

# The FooterLinks model takes advantage of the RelatedLink model we implemented above.

@register_setting
class FooterLinks(BaseSetting, ClusterableModel):

    panels = [
        InlinePanel('footer_links', label="Footer Links"),
    ]

class FooterLinksRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('FooterLinks', related_name='footer_links')

# RE the SiteBranding model, you'll note that there's no custom-validation on the
# banner_colour field to check that a valid hex value has been entered. This would
# probably be better off as a select field with a set of predefined colour choices.

@register_setting
class SiteBranding(BaseSetting):
    site_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    banner_colour = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        help_text="Fill in a hex colour value"
    )

    panels = [
        ImageChooserPanel('site_logo'),
        FieldPanel('banner_colour'),
    ]
