from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete


def upload_location(instance , filename , **kwargs):
    file_path = 'blog/{user_id}/{name}- {filename}'.format(
        user_id      = str(instance.user.id),
        name         = str(instance.name),
        filename     = filename
    )

    return file_path
    


class Profile(models.Model):
    user                    = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    name                    = models.CharField(max_length=60)
    contact                 = models.CharField(max_length=15)
    date_of_birth           = models.DateField(verbose_name="birth date",blank = False);
    image                   = models.ImageField(upload_to = upload_location ,default = 'download.png')

    objects = models.Manager()

    def __str__(self):
        return self.name

@receiver(post_delete, sender = Profile)
def submission_delete(sender , instance , **kwargs):
    instance.image.delete(False)


