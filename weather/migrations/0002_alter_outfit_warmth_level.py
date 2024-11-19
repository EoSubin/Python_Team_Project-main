# Generated by Django 5.1.3 on 2024-11-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='warmth_level',
            field=models.IntegerField(choices=[(1, 'Level 1: 매우 더운 날씨 (30°C 이상)'), (2, 'Level 2: 더운 날씨 (23°C ~ 29°C)'), (3, 'Level 3: 선선한 날씨 (15°C ~ 22°C)'), (4, 'Level 4: 쌀쌀한 날씨 (5°C ~ 14°C)'), (5, 'Level 5: 매우 추운 날씨 (0°C 이하)')]),
        ),
    ]