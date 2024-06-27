# Generated by Django 5.0.6 on 2024-06-19 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewards',
            name='rewardsStatus',
            field=models.CharField(choices=[('REJECTED', 'Rejected'), ('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('CANCELLED', 'Cancelled'), ('COMPLETE', 'Complete'), ('AVAILABLE', 'Available'), ('REDEEMED', 'Redeemed'), ('ON_HOLD', 'On Hold'), ('EXPIRED', 'Expired'), ('IN_PROGRESS', 'In Progress')], max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='rewards',
            unique_together={('username', 'title')},
        ),
    ]