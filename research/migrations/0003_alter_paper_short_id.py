# Generated by Django 4.1.7 on 2023-04-02 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0002_remove_paper_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='short_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]