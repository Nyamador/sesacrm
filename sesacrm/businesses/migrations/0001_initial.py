# Generated by Django 2.2.5 on 2019-10-03 03:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Business Name')),
                ('business_type', models.CharField(max_length=2, verbose_name='Business Type')),
                ('number', models.IntegerField(verbose_name='Mobile Number')),
                ('telephone', models.IntegerField(blank=True, null=True, verbose_name='Mobile Number 2')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('digital_address', models.CharField(max_length=10, verbose_name='Digital Address')),
                ('business_address', models.CharField(max_length=10, verbose_name='Business Address')),
                ('business_reg', models.CharField(max_length=10, verbose_name='Digital Registration Number')),
                ('contact_name', models.CharField(max_length=10, verbose_name='Business Contact Person')),
                ('tin', models.CharField(max_length=10, verbose_name='Tax Identification Number')),
                ('approved', models.BooleanField(default=False, verbose_name='Approved?')),
            ],
        ),
        migrations.CreateModel(
            name='CrmCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]