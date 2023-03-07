# Generated by Django 4.1.7 on 2023-03-07 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_listdo_color_bg'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('list_removed', models.BooleanField(default=False)),
                ('ping', models.BooleanField(default=False)),
                ('list_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='listdo',
            name='list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Home.list'),
            preserve_default=False,
        ),
    ]
