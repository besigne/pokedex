# Generated by Django 3.2.6 on 2021-08-28 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='evolution',
            field=models.ManyToManyField(blank=True, to='core.Evolution'),
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='type',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type',
            field=models.ManyToManyField(to='core.Type'),
        ),
    ]