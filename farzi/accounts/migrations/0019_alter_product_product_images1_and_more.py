# Generated by Django 4.2.2 on 2023-09-08 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_product_product_images1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_images1',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='sample/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_images2',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='sample/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_images3',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='sample/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_images4',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='sample/'),
        ),
    ]
