# Generated by Django 2.1.2 on 2018-10-29 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_testpurpose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='testPurpose',
        ),
    ]
