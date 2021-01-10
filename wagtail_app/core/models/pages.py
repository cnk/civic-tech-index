from rest_framework import serializers

from wagtail.api import APIField
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.embeds.blocks import EmbedBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.admin.edit_handlers import StreamFieldPanel

from .blocks import CustomImageChooserBlock, HeadingBlock
from .faq import FAQBlock


class BasicPage(Page):
    body = StreamField([
        ('heading', HeadingBlock(group="General")),
        ('paragraph', blocks.RichTextBlock(group="General")),
        ('email', blocks.EmailBlock(group="General")),
        ('url', blocks.URLBlock(group="General")),
        ('page', blocks.PageChooserBlock(group="General")),
        ('document', DocumentChooserBlock(group="General")),
        ('image', CustomImageChooserBlock(group="General")),
        ('video', EmbedBlock(group="General")),
        ('faqs', FAQBlock(group="Special")),
    ])

    content_panels = Page.content_panels + [StreamFieldPanel("body", classname="full")]

    api_fields = (
        'body',
        APIField("pub_date", serializer=serializers.DateTimeField(format="%d %B %Y", source="last_published_at")),
    )
