# Generated by Django 3.1.4 on 2021-01-08 06:07

import core.models.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('core', '0002_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('style', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'Heading 2'), ('h3', 'Heading 3'), ('h4', 'Heading 4')], requried=True)), ('centered', wagtail.core.blocks.BooleanBlock(default=False, help_text='Check this box to center the header text.', required=False))], group='General')), ('paragraph', wagtail.core.blocks.RichTextBlock(group='General')), ('email', wagtail.core.blocks.EmailBlock(group='General')), ('url', wagtail.core.blocks.URLBlock(group='General')), ('page', wagtail.core.blocks.PageChooserBlock(group='General')), ('document', wagtail.documents.blocks.DocumentChooserBlock(group='General')), ('image', core.models.blocks.CustomImageChooserBlock(group='General')), ('video', wagtail.embeds.blocks.EmbedBlock(group='General')), ('faqs', wagtail.core.blocks.StructBlock([('show', wagtail.core.blocks.IntegerBlock(default=5, help_text='Display this many FAQs in the block.', label='Number of FAQs to Display'))], group='Special'))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
