from django.db import models
from django_postgres_extensions.models.fields import ArrayField
import uuid
# Create your models here.

class LoginDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length = 40)
    password = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)

class UserData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(LoginDetails, on_delete=models.CASCADE)
    prediction = models.CharField(max_length = 20)
    percentage = models.FloatField()
 
class Records(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    data = ArrayField(models.BooleanField())
