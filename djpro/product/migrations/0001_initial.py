# Generated by Django 2.0.2 on 2018-06-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('del_flag', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200, verbose_name='book name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='book price')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
