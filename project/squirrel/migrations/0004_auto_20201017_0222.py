# Generated by Django 3.1.2 on 2020-10-17 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0003_auto_20201016_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Approaches',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Chasing',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Climbig',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Eating',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Foraging',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Indifferent',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Kuks',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Location',
            field=models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Moans',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Other_Activities',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnamon', 'Cinnamon')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Quaas',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Running',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Runs_from',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Shift',
            field=models.CharField(choices=[('PM', 'PM'), ('AM', 'AM')], max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Specific_Location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Tail_flags',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
