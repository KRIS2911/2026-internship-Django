from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.IntegerField()
    join_date=models.DateTimeField(auto_now_add=True)
    post=models.CharField(max_length=100)

    class Meta:
        db_table='employee'

    def __str__(self):
        return self.name
    