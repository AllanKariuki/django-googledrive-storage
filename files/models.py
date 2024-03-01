from django.db import models

from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

class File(models.Model):
    file_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/', storage=gd_storage)

    def __str__(self):
        return self.name

