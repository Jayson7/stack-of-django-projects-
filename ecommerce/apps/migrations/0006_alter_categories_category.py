# Generated by Django 3.2.7 on 2021-09-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_categories_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(choices=[('food', 'food'), ('shoes', 'shoes'), ('clothes', 'clothes')], default='selcect a category', max_length=40),
        ),
    ]
