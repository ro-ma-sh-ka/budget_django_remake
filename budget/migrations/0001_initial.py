# Generated by Django 4.1.5 on 2023-01-04 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='budget.familymember')),
                ('editor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='budget.familymember')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='budget.familymember')),
                ('editor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='budget.familymember')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('total', models.FloatField()),
                ('what_is', models.TextField(max_length=200)),
                ('public', models.BooleanField(default=True)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='budget.familymember')),
                ('currency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='budget.currency')),
                ('editor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='budget.familymember')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='budget.section')),
            ],
        ),
    ]