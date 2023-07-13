# Generated by Django 4.1.10 on 2023-07-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=255)),
                ('class_attended', models.IntegerField(default=0)),
                ('total_classes', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('offline', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='DemoClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url_link', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('offline_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('online_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
            ],
        ),
        migrations.CreateModel(
            name='JobPortal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_title', models.CharField(max_length=300)),
                ('location', models.CharField(default='eranakulam', max_length=200)),
                ('salary', models.PositiveIntegerField()),
                ('bond', models.PositiveIntegerField()),
                ('url_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='LiveClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=300)),
                ('trainer_name', models.CharField(max_length=300)),
                ('time', models.TimeField()),
                ('status', models.BooleanField(default=True)),
                ('url_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('mod1_text', models.TextField()),
                ('mod2_text', models.TextField()),
                ('mod3_text', models.TextField()),
                ('mod4_text', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('online_fees', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('offline_fees', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('batch_code', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=255)),
                ('subjects', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=300)),
                ('test_title', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('total_mark', models.PositiveIntegerField(default=100)),
                ('obtained_mark', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VideoScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]
