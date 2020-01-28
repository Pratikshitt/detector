# Generated by Django 2.2.7 on 2020-01-28 12:47

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_auto_20200121_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='Symptoms',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Headache'), (2, 'Sore Throat'), (3, 'Sneezing'), (4, 'Earache'), (5, 'Muscle Pain'), (6, 'Fever'), (7, 'Vomiting'), (8, 'Cough'), (9, 'Weight Loss'), (10, 'Dehydration'), (11, 'Stomachache'), (12, 'Sweet And Chill'), (13, 'Tiredness'), (14, 'Loss of Apetite'), (15, 'Greyish White Spot on Cheek'), (16, 'Constipation'), (17, 'Hairloss'), (18, 'Sore Tongue'), (19, 'Shortness in Breathe'), (20, 'Dysphagia'), (21, 'Red Spots'), (22, 'Wheezing'), (23, 'TightChest'), (24, 'Swolen Abdomen'), (25, 'Hydrophobia'), (26, 'Rashes'), (27, 'Rice Watery Stool'), (28, 'Dry Mouth'), (29, 'Rapid Heart Rate'), (30, 'Redness of Eye'), (31, 'Lymphadenopathy')], max_length=83),
        ),
    ]
