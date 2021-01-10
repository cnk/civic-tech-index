from wagtail.core import blocks
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.blocks import ImageChooserBlock


class HeadingBlock(blocks.StructBlock):
    STYLES = [
        ('h2', 'Heading 2'),
        ('h3', 'Heading 3'),
        ('h4', 'Heading 4'),
    ]

    text = blocks.CharBlock(required=True)
    style = blocks.ChoiceBlock(
        choices=STYLES,
        requried=True,
        default='h3'
    )
    centered = blocks.BooleanBlock(
        required=False,
        default=False,
        help_text='Check this box to center the header text.'
    )

    class Meta:
        label = 'Heading'
        template = 'core/blocks/header-block.html'
        form_classname = 'section-title struct-block'
        icon = 'fa-header'


class CustomImageChooserBlock(ImageChooserBlock):
    def __init__(self, *args, **kwargs):
        self.rendition = kwargs.pop("rendition", "original")
        super().__init__(**kwargs)

    def get_api_representation(self, value, context=None):
        return ImageRenditionField(self.rendition).to_representation(value)
