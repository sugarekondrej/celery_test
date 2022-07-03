from django.db import models

# Create your models here.
class BillingItem(models.Model):
    item_name = models.CharField(max_length=120, blank=True,null=True)
    number_1=models.IntegerField()
    number_2=models.IntegerField()
    total = models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return f"{self.total}"
    
    def __str__(self):
         return f"{self.total}"