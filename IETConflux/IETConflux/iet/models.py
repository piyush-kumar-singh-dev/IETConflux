from django.db import models
from django.core.validators import FileExtensionValidator
class Subject(models.Model):
    Topicname=models.CharField(max_length=100, help_text='Topic of the Subject')
    Subjname = models.CharField(max_length=100, help_text='Name of the Subject')
    Authname = models.CharField(max_length=100, help_text='Author of the Subject')
    image= models.FileField(validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    def __str__(self):
        return self.Subjname+' '+self.Authname

class Notes(models.Model):
    notes_id= models.ForeignKey(Subject,on_delete=models.CASCADE)
    notedetails=models.CharField(max_length=1000, help_text='What is in the notes')
    Subjname = models.CharField(max_length=100, help_text='Name of the Subject')
    Authname = models.CharField(max_length=100, help_text='Author of the Subject')
    Authbranch = models.CharField(max_length=100, help_text='Branch of the author')
    file = models.FileField(validators=[FileExtensionValidator(['pdf','docs','doc','docx','txt','djvu','epub','chm'])])
    def __str__(self):
        return self.Subjname+' '+self.Authname+' '+self.Authbranch





