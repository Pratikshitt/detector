from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class topic(models.Model):
    top_name=models.CharField(max_length=234,unique= True)

    def __str__(self):
        return(self.top_name)


class webpage(models.Model):
    #topic=models.ForeignKey(topic)
    name=models.CharField(max_length=234)
    url=models.URLField(unique=True)

    def __str__(self):
        return(self.name)

class ModelForm(models.Model):
    Name=models.CharField(max_length=234)
    Email=models.EmailField(unique=True)

    def __str__(self):
        return(self.Name,self.Email)  

MY_CHOICES2 = ((1, 'Headache'),
               (2, 'Sore Throat'),
               (3, 'Sneezing'),
               (4, 'Earache'),
               (5, 'Muscle Pain'),
               (6,'Fever'),
               (7,'Vomiting'),
               (8, 'Cough'),
               (9, 'Weight Loss'),
               (10, 'Dehydration'),
               (11, 'Stomachache'),
               (12, 'Sweet And Chill'),
               (13, 'Tiredness'),
               (14, 'Loss of Apetite'),
               (15, 'Greyish White Spot on Cheek'),
               (16, 'Constipation'),
               (17, 'Hairloss'),
               (18, 'Sore Tongue'),
               (19, 'Shortness in Breathe'),
               (20, 'Dysphagia'),
               (21, 'Red Spots'),
               (22, 'Wheezing'),
               (23, 'TightChest'),
               (24, 'Swolen Abdomen'),
               (25, 'Hydrophobia'),
               (26, 'Rashes'),
               (27, 'Rice Watery Stool'),
               (28, 'Dry Mouth'),
               (29, 'Rapid Heart Rate'),
               (30, 'Redness of Eye')
             
               
               )
             
               


class MyModel(models.Model):      
    Symptoms = MultiSelectField(choices=MY_CHOICES2,blank=True)
    #  Days=models.IntegerField()
    Days= models.IntegerField(null=False ,blank=True)


class GeneralRemedies(models.Model):
    Diseasename=models.CharField(max_length=2225)
    Remedies=models.CharField(max_length=2225)

class AuyervedicRemedies(models.Model):
    Diseasenam=models.CharField(max_length=2225)
    Remedie=models.CharField(max_length=2225)
    


