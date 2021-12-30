from django.db import models

class PhoneModel(models.Model):
    Pname = models.CharField(max_length=100)
    Porigin = models.CharField(max_length=100)
    Pyear = models.IntegerField()
    Pabout = models.TextField()

    def __str__(self):
        return self.Pname

class ModelDetail(models.Model):
    mname = models.CharField(max_length=100)
    mprice = models.IntegerField()
    mabout = models.TextField()
    phonemodel = models.ForeignKey(PhoneModel,related_name="model",on_delete=models.CASCADE)