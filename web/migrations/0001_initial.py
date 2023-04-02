# Generated by Django 4.1.7 on 2023-04-02 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('last_name', models.CharField(blank=True, max_length=80, null=True)),
                ('father', models.CharField(blank=True, max_length=30, null=True)),
                ('birthday', models.CharField(blank=True, max_length=20, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=35, null=True)),
                ('create_card_place', models.CharField(blank=True, max_length=35, null=True)),
                ('Sericard', models.CharField(blank=True, max_length=35, null=True)),
                ('Serialcard', models.CharField(blank=True, max_length=35, null=True)),
                ('Fatherseri', models.CharField(blank=True, max_length=35, null=True)),
                ('Fatherserial', models.CharField(blank=True, max_length=35, null=True)),
                ('Motherseri', models.CharField(blank=True, max_length=35, null=True)),
                ('Motherserial', models.CharField(blank=True, max_length=35, null=True)),
                ('nin', models.CharField(blank=True, max_length=12, null=True)),
                ('home_phone', models.CharField(blank=True, max_length=35, null=True)),
                ('home_code', models.CharField(blank=True, max_length=35, null=True)),
                ('city', models.CharField(blank=True, max_length=35, null=True)),
                ('province', models.CharField(blank=True, max_length=35, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('father_father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('father_nin', models.CharField(blank=True, max_length=12, null=True)),
                ('father_education', models.CharField(blank=True, max_length=35, null=True)),
                ('father_phone', models.CharField(blank=True, max_length=35, null=True)),
                ('father_work', models.CharField(blank=True, max_length=35, null=True)),
                ('father_birth', models.CharField(blank=True, max_length=20, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_nin', models.CharField(blank=True, max_length=12, null=True)),
                ('mother_education', models.CharField(blank=True, max_length=35, null=True)),
                ('mother_work', models.CharField(blank=True, max_length=35, null=True)),
                ('mother_phone', models.CharField(blank=True, max_length=35, null=True)),
                ('mother_birth', models.CharField(blank=True, max_length=20, null=True)),
                ('telegram_phone', models.CharField(blank=True, max_length=35, null=True)),
                ('e_place', models.CharField(blank=True, choices=[('مهد شکوفه', 'مهد شکوفه'), ('پیش دبستانی بهاران', 'پیش دبستانی بهاران')], max_length=30, null=True)),
                ('Hand', models.CharField(blank=True, max_length=35, null=True)),
                ('Talagh', models.CharField(blank=True, max_length=35, null=True)),
                ('Shahid', models.CharField(blank=True, max_length=35, null=True)),
                ('Bimeh', models.CharField(blank=True, max_length=35, null=True)),
                ('Farhangi', models.CharField(blank=True, max_length=35, null=True)),
                ('Children', models.CharField(blank=True, max_length=35, null=True)),
                ('Child', models.CharField(blank=True, max_length=35, null=True)),
                ('credit', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('pay', models.BooleanField(blank=True, default=False, null=True)),
                ('yearadded', models.CharField(blank=True, default='1401', max_length=6, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
