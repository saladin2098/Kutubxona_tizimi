# Generated by Django 4.0.4 on 2022-05-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_alter_subject_speciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(null=True, to='university.teacher'),
        ),
    ]
