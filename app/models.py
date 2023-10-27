from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=150)
    instruments = (('piano', 'piano'), ('guitar', 'guitar'))
    instrument = models.CharField(choices=instruments, max_length=150)
    marks_avg = models.DecimalField(max_digits=3, decimal_places=1, default=6.0)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.surname}"

