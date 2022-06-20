# Generated by Django 4.0.4 on 2022-06-18 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='target_ct',
            field=models.ForeignKey(blank=True, limit_choices_to={'id__gte': 13}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_obj', to='contenttypes.contenttype'),
        ),
    ]
