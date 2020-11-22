# Generated by Django 3.1.2 on 2020-11-21 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Node',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
