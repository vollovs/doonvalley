from django.db import models
import uuid

class Member(models.Model):
    BASKETBALL = 'BB'
    BADMINTON = 'BA'
    
    CLUB = (
        (BASKETBALL, 'Basketball'),
        (BADMINTON, 'Badminton'),
    )
    
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    chinese_name = models.CharField(max_length=60, blank=True, null=False)
    english_name = models.CharField(max_length=60, blank=True, null=False)
    email = models.EmailField(max_length=60, blank=True, null=False)
    phone = models.CharField(max_length=160, blank=True, null=True)
    
    club = models.CharField(max_length=2,
                                      choices=CLUB,
                                      default=BASKETBALL)
    
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.chinese_name
        
class MemberHistory(models.Model):
    member = models.ForeignKey('Member')
    year = models.CharField(max_length=4, blank=False, null=False)
    
    
