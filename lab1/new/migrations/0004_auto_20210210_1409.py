# Generated by Django 3.1.6 on 2021-02-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0003_auto_20210210_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='category',
            name='categoryId',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='productId',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
