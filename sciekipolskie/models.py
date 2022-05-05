from django.db import models

# Create your models here.
class ListOfWorkers(models.Model):
    name = models.CharField(max_length=255)
    id_of_worker = models.CharField(max_length=255)

class EmployeeTaskDescription(models.Model):
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=15)
    category = models.CharField(max_length=30)
    deadline = models.DateField()
    done_btn = models.BooleanField(default=False)
    # worker_id = models.ForeignKey(ListOfWorkers, on_delete=models.CASCADE)