from django.db import models # type: ignore

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=100,default=None,null=True, blank=True)
    pic = models.CharField(max_length=1000,default=None,null=True, blank=True)
    url1 = models.CharField(max_length=1000,default=None,null=True, blank=True)
    url2 = models.CharField(max_length=1000,default=None,null=True, blank=True)
    url3 = models.CharField(max_length=1000,default=None,null=True, blank=True)
    url4 = models.CharField(max_length=1000,default=None,null=True, blank=True)
    url5 = models.CharField(max_length=1000,default=None,null=True, blank=True)
    url6 = models.CharField(max_length=1000,default=None,null=True, blank=True)
    url7 = models.CharField(max_length=1000,default=None,null=True, blank=True)
    url8 = models.CharField(max_length=1000,default=None,null=True, blank=True)
    url9 = models.CharField(max_length=1000,default=None,null=True, blank=True)
    url10 = models.CharField(max_length=1000,default=None,null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
