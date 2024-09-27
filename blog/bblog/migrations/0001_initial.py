# Generated by Django 5.1 on 2024-09-11 08:29

import django.db.models.deletion
import django.utils.timezone
import markdownx.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BigCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SmallCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bblog.bigcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('thumbnail', models.ImageField(default='A28WZDTYEY.jpg', upload_to='media', verbose_name='サムネイル')),
                ('text', markdownx.models.MarkdownxField(help_text='Markdown形式で書いてください。', verbose_name='本文')),
                ('card_text', markdownx.models.MarkdownxField(help_text='Markdown形式で書いてください。', null=True, verbose_name='記事説明文')),
                ('is_public', models.BooleanField(default=True, verbose_name='公開可能か')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('live', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Category', to='bblog.smallcategory')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
