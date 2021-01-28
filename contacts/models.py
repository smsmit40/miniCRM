from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=75)
    Phone = models.CharField(max_length=15)
    Notes= models.TextField()

    def __str__(self):
        return self.Name

class Files(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="media")
    file_notes = models.TextField()

    def __str__(self):
        return self.file.name

class Email(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    Attachment = models.ForeignKey(Files, null=True, blank=True, on_delete=models.SET_NULL)
    subject = models.CharField(max_length=250)
    message = models.TextField()

class Reminder(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    Details = models.TextField()
    Date = models.DateField(null=True, blank=True)
    Time = models.TimeField(null=True, blank=True)
