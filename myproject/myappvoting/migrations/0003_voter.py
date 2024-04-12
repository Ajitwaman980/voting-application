# Generated by Django 5.0 on 2024-04-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappvoting', '0002_contact_delete_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar', models.CharField(max_length=12, unique=True)),
                ('vote', models.CharField(choices=[('BJP', 'BJP'), ('CONGRESS', 'Congress'), ('AAP', 'AAP'), ('SHIVSENA', 'Shivsena')], max_length=20)),
            ],
        ),
    ]