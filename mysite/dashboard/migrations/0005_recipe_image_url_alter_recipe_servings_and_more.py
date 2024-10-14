# Generated by Django 5.1.1 on 2024-10-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_recipe_servings_recipe_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image_url',
            field=models.CharField(max_length=300, null=True, verbose_name='이미지 링크'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(null=True, verbose_name='인분'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(null=True, verbose_name='요리 시간'),
        ),
    ]
