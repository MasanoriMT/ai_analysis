# Generated by Django 3.0.14 on 2021-04-17 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AiAnalysisLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(blank=True, max_length=255, null=True)),
                ('success', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('class_field', models.IntegerField(blank=True, db_column='class', null=True)),
                ('confidence', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('request_timestamp', models.PositiveIntegerField(blank=True, null=True)),
                ('response_timestamp', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ai_analysis_log',
            },
        ),
    ]