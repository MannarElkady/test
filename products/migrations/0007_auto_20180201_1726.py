# Generated by Django 2.0 on 2018-02-01 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='ItemReview',
            new_name='Review',
        ),
    ]