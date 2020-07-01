from django.db import models

# Create your models here.
class Bank(models.Model):
    bankName = models.CharField(max_length=50)

    class Meta:
        order_with_respect_to = ('bankName', )

    def __str__(self):
        return "{}".format(self.bankName)

class Branch(models.Model):
    branchName = models.CharField(max_length=200)
    ifsc_code = models.CharField(max_length=500, unique=True)
    bank = models.ForeignKey(Bank)
    branchAddress = models.CharField(max_length=500)
    branchCity = models.CharField(max_length=500)
    branchDistrict = models.CharField(max_length=500)
    branchState = models.CharField(max_length=500)

    class Meta:
        order_with_respect_to = ('branchName',)
        verbose_name = 'Branch'
        verbose_name_plural = 'Branch'

    def __str__(self):
        return "{} - {} - {}".format(self.branchName, self.branchCity, self.bank)