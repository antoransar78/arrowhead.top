# Generated by Django 5.0.6 on 2024-07-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_slideritem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('service_rating', models.CharField(choices=[('excellent', 'Excellent'), ('super', 'Super'), ('good', 'Good'), ('okey', 'Okey'), ('not satisfactory', 'Not Satisfactory')], max_length=16)),
                ('food_rating', models.CharField(choices=[('excellent', 'Excellent'), ('super', 'Super'), ('good', 'Good'), ('okey', 'Okey'), ('not satisfactory', 'Not Satisfactory')], max_length=16)),
                ('drinks_rating', models.CharField(choices=[('excellent', 'Excellent'), ('super', 'Super'), ('good', 'Good'), ('okey', 'Okey'), ('not satisfactory', 'Not Satisfactory')], max_length=16)),
                ('ambience_rating', models.CharField(choices=[('excellent', 'Excellent'), ('super', 'Super'), ('good', 'Good'), ('okey', 'Okey'), ('not satisfactory', 'Not Satisfactory')], max_length=16)),
                ('cleanliness_rating', models.CharField(choices=[('excellent', 'Excellent'), ('super', 'Super'), ('good', 'Good'), ('okey', 'Okey'), ('not satisfactory', 'Not Satisfactory')], max_length=16)),
                ('comments', models.TextField(blank=True, null=True)),
                ('order', models.CharField(choices=[('steak', 'Steak'), ('platter', 'Platter'), ('chicken', 'Chicken'), ('Table Top', 'Table Top')], max_length=16)),
                ('compliments', models.TextField(blank=True, null=True)),
                ('visit_reason', models.CharField(choices=[('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('By Friend', 'By Friend'), ('Google Reviews', 'Google Reviews')], max_length=100)),
                ('heard_about_us', models.CharField(choices=[('First Visit', 'First Visit'), ('Second Visit', 'Second Visit'), ('Third Visit', 'Third Visit'), ('Multiple Visit', 'Multiple Visit')], max_length=100)),
            ],
        ),
    ]
