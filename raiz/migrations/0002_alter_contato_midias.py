# Generated by Django 3.2.7 on 2021-10-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='midias',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/%Y/%m'),
        ),
    ]
