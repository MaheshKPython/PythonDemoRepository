from django.db import models
from django.util

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sal = models.FloatField()

    class Meta:
        db_table = 'emp_info'

    def __eq__(self, other):
        return self.id == other.id and \
               self.name == other.name and \
               self.age == other.age and \
               self.sal == other.sal


class Address(models.Model):
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()
    emp = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='adrref', null=True)

    class Meta:
        db_table = 'adr_info'

    def __eq__(self, other):
        return self.id == other.id and \
               self.city == other.city and \
               self.state == other.state and \
               self.pincode == other.pincode


<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

<!-- jQuery and JS bundle w/ Popper.js -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>