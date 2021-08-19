from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    notification = models.TextField(max_length=100)
    is_seen = models.BooleanField(default=False)

    # override save method
    def save(self, *args, **kwargs):
        print("save and call")
        super(Notification,self).save(*args,**kwargs)

    # class Meta:
    #     db_table = "Notification"