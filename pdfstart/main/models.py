from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
class Accounts(models.Model):
    user_name = models.CharField(max_length=60)
    user_email = models.CharField(max_length=60)
    user_date_registration = models.DateField()
    user_count_uploads = models.IntegerField(default=0)

class Files(models.Model):
    author_file = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)
    file_name = models.CharField(max_length=60)
    file_upload = models.DateField()
    file_size = models.IntegerField()

@receiver(post_save, sender=Files)
def increment_user_count_uploads(sender, instance, **kwargs):
    if instance.author_file:
        instance.author_file.user_count_uploads += 1
        instance.author_file.save()
# Create your models here.
