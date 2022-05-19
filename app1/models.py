from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=30)
    guruh = models.CharField(max_length=20)
    guvohnoma = models.CharField(max_length=10, blank=True)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    bitiruvchi = models.BooleanField(blank=True,default=False)
    def __str__(self):
        return self.ism

class Muallif(models.Model):
    nomi = models.CharField(max_length=60)
    ism = models.CharField(max_length=60)
    tirik = models.BooleanField()
    yosh = models.PositiveSmallIntegerField( )
    jins= models.CharField(max_length=10 , choices=(( "male" , "male") , ("female" , "female")))
    kitoblar_soni = models.PositiveSmallIntegerField( default=1)
    def __str__(self):
        return self.ism
class kitob(models.Model):
    nomi = models.CharField(max_length=60)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=70)
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE)
    def __str__(self):
        return self.nomi
class record(models.Model):
    sana = models.DateField(null=True)
    student =models.ForeignKey(Student , on_delete=models.CASCADE)
    kitob = models.ForeignKey(kitob, on_delete=models.CASCADE)
    qaytardi = models.CharField(max_length=5, choices=(("Ha", "Ha"), ("Yo'q", "Yo'q")))
    qaytarish_sana = models.DateField(null=True )

    def __str__(self):
        return f" {self.student.ism} ,{self.kitob.nomi}"