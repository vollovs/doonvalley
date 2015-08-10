from django.db import models
import uuid

class Member(models.Model):
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    chinese_name = models.CharField(max_length=60, blank=True, null=False)
    english_name = models.CharField(max_length=60, blank=True, null=False)
    email = models.EmailField(max_length=60, blank=True, null=False)
    phone = models.CharField(max_length=160, blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title

class MemberHistory(models.Model):
    member = models.ForeignKey('Member')
    created = models.DateTimeField(auto_now_add=True)
    
    # return year number when join the club 
    def attending_year(self):
        return ''
    
# Events .
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver

@receiver(pre_save, sender=Member)
def auto_save_member_on_update(sender, instance, **kwargs):
    """Save member into MemberHistory when setting member to active
    """
    instance.image.delete(False)