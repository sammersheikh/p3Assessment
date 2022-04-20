# Generated by Django 4.0.2 on 2022-04-20 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget', models.CharField(choices=[('1', 'Widget1'), ('2', 'Widget2'), ('3', 'Widget3'), ('4', 'Widget4'), ('5', 'Widget5')], default='1', max_length=1)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
    ]
