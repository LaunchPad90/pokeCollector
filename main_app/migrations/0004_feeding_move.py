# Generated by Django 3.0.3 on 2020-03-19 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200319_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Pokemon')),
            ],
        ),
    ]
