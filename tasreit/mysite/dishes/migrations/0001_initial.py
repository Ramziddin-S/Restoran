# Generated by Django 3.2.4 on 2021-06-10 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_your_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=210)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(default=0)),
                ('check_in', models.CharField(max_length=120)),
                ('time', models.CharField(max_length=123)),
                ('guest', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=123)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Our_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='Recent_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('Description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Our_menu_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('Description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.IntegerField(default=0)),
                ('our_menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dishes.our_menu')),
            ],
        ),
    ]
