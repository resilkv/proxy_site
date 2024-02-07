from django.db import models

class ProxyList(models.Model):
    
    ip_address = models.CharField(max_length=250,null=True,blank=True)
    port = models.CharField(max_length=250,null=True,blank=True)
    protocol = models.CharField(max_length=250,null=True,blank=True)
    country = models.CharField(max_length=250,null=True,blank=True)
    uptime = models.CharField(max_length=250,null=True,blank=True)
    
    def __str__(self):
        return self.ip_address