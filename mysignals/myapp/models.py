from django.db import models
from django.db.models.signals import pre_delete,post_save
from django.dispatch import receiver

class Mysignal(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self)->str:
        return self.name
    

@receiver(post_save,sender=Mysignal)
def mysignal_post_save(sender, instance,**kwrgs):
    print('mysignal instance was saved')


@receiver(pre_delete, sender=Mysignal)
def mysignal_pre_delete(sender,  instance,**kwrgs):
    print('mysignal instance is about deleted')

    