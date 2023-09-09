# Generated by Django 4.2.2 on 2023-09-06 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_category_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=255)),
                ('product_images1', models.ImageField(blank=True, max_length=255, null=True, upload_to='product')),
                ('product_images2', models.ImageField(blank=True, max_length=255, null=True, upload_to='product')),
                ('product_images3', models.ImageField(blank=True, max_length=255, null=True, upload_to='product')),
                ('product_images4', models.ImageField(blank=True, max_length=255, null=True, upload_to='product')),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]