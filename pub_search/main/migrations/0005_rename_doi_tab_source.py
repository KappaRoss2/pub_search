# Generated by Django 4.0.4 on 2022-06-16 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_tab_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tab',
            old_name='doi',
            new_name='source',
        ),
    ]
