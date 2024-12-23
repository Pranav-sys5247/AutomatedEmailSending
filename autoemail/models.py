from django.db import models
# Create your models here.
class birthday(models.Model):
    sender_email = models.EmailField(max_length=255)
    receiver_email = models.EmailField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='uploads/images/')
    
    class Meta:
        db_table = "births"  # Use '=' to define table name
