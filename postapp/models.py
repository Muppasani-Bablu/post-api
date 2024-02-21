from django .db import models
class Model(models.Model):
    student=models.CharField(max_length=255)
    sno=models.AutoField (primary_key=True)
    classroom=models.IntegerField()
    def __str__(self): 
        return self.student
    class Meta:
        db_table="helo"  
        managed=True   

# from django.db import models

# # Create your models here.
# class Model (models.Model):
#     id=models.AutoField(primary_key=True)
#     salary=models.BigIntegerField()
    
    
#     def __str__(self):
#         return self.id
#     class Meta:
#         db_table="helo"
#         managed=False
