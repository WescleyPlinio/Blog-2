# Generated by Django 5.1.2 on 2024-11-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_facebook_alter_blog_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subnome',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]