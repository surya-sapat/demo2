# Generated by Django 3.2.20 on 2023-08-08 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0028_flex_peer_ora_course_setting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalcourseoverview',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical course overview', 'verbose_name_plural': 'historical course overviews'},
        ),
    ]