# Generated by Django 5.0.6 on 2024-06-26 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'Very poor'), (2, 'Poor'), (3, 'Average'), (4, 'Good'), (5, 'Execellent')])),
                ('review', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', to_field='name')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
            options={
                'unique_together': {('product', 'username')},
            },
        ),
    ]
