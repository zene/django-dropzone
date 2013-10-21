import string
import random

from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField


def key_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class DropzoneImage(models.Model):
    """Model for storing uploaded photos"""
    # Put a foreign key to the model you want these uploaded images to belong to,
    #   or create a intermediary table, or whatever you want to do. I'm not your Mom.
    image = ThumbnailerImageField(upload_to='dropzone_img')
    key = models.CharField(max_length=6, unique=True, db_index=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def generate_key(self):
        """returns a six character unique key"""
        while 1:
            key = key_generator()
            try:
                DropzoneImage.objects.get(key=key)
            except:
                return key

    def __unicode__(self):
        return self.image.name
