# Generated by Django 3.2.7 on 2021-10-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_categories_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(choices=[('shoes', 'shoes'), ('food', 'food'), ('clothes', 'clothes')], default='selcect a category', max_length=40),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]