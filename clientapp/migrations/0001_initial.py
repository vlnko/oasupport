# Generated by Django 3.1.7 on 2021-04-10 10:43

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория обращения',
                'verbose_name_plural': 'Категории обращений',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название компании')),
                ('inn', models.CharField(blank=True, max_length=12, null=True, verbose_name='ИНН')),
                ('ogrn', models.CharField(blank=True, max_length=13, null=True, verbose_name='ОГРН')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('title', models.CharField(max_length=32, verbose_name='Название')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
            ],
            options={
                'verbose_name': 'Статус обращения',
                'verbose_name_plural': 'Статусы обращений',
            },
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='', max_length=120, verbose_name='Тема')),
                ('title', models.CharField(max_length=50, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Описание проблемы')),
                ('file', models.FileField(blank=True, null=True, upload_to='media', verbose_name='Файл')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='Дата предполагаемого решения')),
                ('verdict', models.TextField(blank=True, default='', null=True, verbose_name='Вердикт')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Отправлен в архив')),
                ('category', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='clientapp.category', verbose_name='Категория')),
                ('status', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='clientapp.status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('company', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='clientapp.company')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
