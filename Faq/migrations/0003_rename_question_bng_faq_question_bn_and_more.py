# Generated by Django 4.2.18 on 2025-02-01 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faq', '0002_rename_question_bn_faq_question_bng_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='question_bng',
            new_name='question_bn',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='question_esp',
            new_name='question_de',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='question_frn',
            new_name='question_es',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='question_ger',
            new_name='question_fr',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='question_hin',
            new_name='question_hi',
        ),
    ]
