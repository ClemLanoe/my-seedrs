# Generated by Django 4.1.2 on 2023-06-07 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secondary_market', '0002_rename_cycles_cycle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('active_on_forums', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='secondary_market.person')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='secondary_market.person')),
            ],
        ),
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_url', models.CharField(max_length=255)),
                ('post_summary', models.CharField(max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='secondary_market.person')),
            ],
        ),
    ]
