# Generated by Django 5.2.4 on 2025-07-25 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('publication_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(help_text='Enter your email', max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(blank=True, default='first name', max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, default='first name', max_length=200, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_of_birth', models.DateField(blank=True, max_length=200, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='profile picture')),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-date_joined'],
                'permissions': [('can_create_post', 'can add post'), ('can_edit_post', 'can edit post'), ('can_delete_post', 'can delete psot'), ('can_view_post', 'can view post')],
            },
        ),
    ]
