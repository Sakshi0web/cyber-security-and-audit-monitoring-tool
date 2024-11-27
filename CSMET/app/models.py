from django.db import models


# Create your models here.

class projectStrategy(models.Model):
    number = models.IntegerField(null=True)
    projectname = models.CharField(max_length=80, null=True)
    projectiteration = models.CharField(max_length=80, null=True)
    estimatetimeline = models.DateTimeField(max_length=80, null=True)
    lead = models.CharField(max_length=80, null=True)
    automatedvatest = models.CharField(max_length=80, null=True)
    manualtest = models.CharField(max_length=80, null=True)
    performancetest = models.CharField(max_length=80,null=True)
                 
class projectProgress(models.Model): 
    number = models.IntegerField()
    name=models.CharField(max_length=80,null=True)
    iteration = models.CharField(max_length=80, null=True)
   # fk = models.ForeignKey(projectStrategy, on_delete=models.CASCADE)
    startdate = models.DateTimeField(max_length=80, null=True)
    projectautomatedvatest = models.CharField(max_length=80, null=True)
    projectmanualtest = models.CharField(max_length=80, null=True)
    projectperformancetest = models.CharField(max_length=80, null=True)
                                                                         


class projectInduction(models.Model):
    projectname =models.CharField(max_length=80,null=True)
    projectowner =models.CharField(max_length=80,null=True)
    projectnumber=models.IntegerField(null=True)
    date_projectnumber=models.DateTimeField(max_length=80, null=True)
    typeofproject=models.CharField(max_length=80,null=True)
    applicationversion=models.CharField(max_length=80,null=True)
    file_avabilityvarepotfromvender=models.FileField(upload_to="induction/",default=None)
    file_avabilitysafetohostcertificate=models.FileField(upload_to="induction1/",default=None)
    file_avabilitydesignorarchitecturedocumention=models.FileField(upload_to="induction2/",default=None)

    RADIO_CHOICES = [
        ('Yes', 'Yes'),
        ('No','NO'),
    ]
    radio_linkedtopreviousproject = models.CharField(
        max_length=10,
        choices=RADIO_CHOICES,
        default='None'
    )

    RADIO_CHOICES = [
        ('Yes', 'Yes'),
        ('No','NO'),
    ]
    radio_avabilityvarepotfromvender = models.CharField(
        max_length=10,
        choices=RADIO_CHOICES,
        default='None'
    )

    RADIO_CHOICES = [
        ('Yes', 'Yes'),
        ('No','NO'),
    ]
    radio_avabilitydesignorarchitecturedocumention = models.CharField(
        max_length=10,
        choices=RADIO_CHOICES,
        default='None'
    )

    RADIO_CHOICES = [
       ('Yes', 'Yes'),
        ('No','NO'),
    ]
    radio_stagingenvironmentavability = models.CharField(
        max_length=10,
        choices=RADIO_CHOICES,
        default='None'
    )

    RADIO_CHOICES = [
        ('Yes', 'Yes'),
        ('No','NO'),
    ]
    radio_ipwhitelisting = models.CharField(
        max_length=10,
        choices=RADIO_CHOICES,
        default='None'
    )

class ProjectComplition(models.Model):
    number=models.IntegerField()
    name=models.CharField(max_length=80,null=True)
    iteration = models.CharField(max_length=80, null=True)
    startdate = models.DateTimeField(max_length=80, null=True)

class Projectreport(models.Model):
    pronumber=models.IntegerField(null=True)
    proname=models.CharField(max_length=80,null=True)
    proiteration = models.CharField(max_length=80, null=True)
    startdate = models.DateTimeField(max_length=80, null=True)
    enddate=models.DateField(max_length=80,null=True)
    provadetils=models.CharField(max_length=80,null=True)
    proseverit=models.CharField(max_length=80,null=True)
    provaparameters=models.CharField(max_length=80,null=True)

class PstatusGraph(models.Model):
    totalnumberofprojectcomplete = models.IntegerField(null=True)
    year = models.IntegerField(null=True) 


class PmanagementGraph(models.Model):
    projectcompleted = models.IntegerField(null=True)
    underprogress = models.IntegerField(null=True)
    pending = models.IntegerField(null=True)
    ongoing = models.IntegerField(null=True)

class ProjectcomplitionGraph(models.Model):
     priorities = models.CharField(max_length=80,null=True) 
     totalnumberofprojectcomparision = models.IntegerField(null=True)


class preauditGraph(models.Model):
    year = models.IntegerField(null=True) 
    preauditperpormnotreceived = models.IntegerField(null=True) 

class quaterlyGraph(models.Model):    
    year = models.IntegerField(null=True) 
    quaterlyfollowupreportnotreceived = models.IntegerField(null=True) 

class Auditinitiation(models.Model):
    projectnumber = models.IntegerField(null=True) 
    unit = models.CharField(max_length=80, null=True)
    station = models.TextField(max_length=80, null=True)
    detailsofitassests = models.CharField(max_length=80, null=True)
    teamdetails = models.CharField(max_length=80, null=True)
    inititationdate = models.DateTimeField(max_length=80,null=True)    

class auditscheduling(models.Model):
    auditschedulingyear=models.IntegerField( null=True)
    file_upload=models.FileField(upload_to="scheduling/",default=None)
    unit=models.CharField(max_length=80,null=True)
    station=models.CharField(max_length=80,null=True)
    auditfrom=models.DateField(max_length=80,null=True)
    auditto=models.DateField(max_length=80,null=True)   

class auditcomplition(models.Model):
    projectnumber = models.IntegerField(null=True)
    unit = models.CharField(max_length=80,null=True)
    station=models.CharField(max_length=80,null=True)
    initiationdate=models.DateField(max_length=80,null=True)
    complitiondate=models.DateField(max_length=80,null=True) 
    file_selectexcelfile=models.FileField(upload_to="complition/",default=None)    
    file_finalauditreport=models.FileField(upload_to="complition1/",default=None)

class auditexecution(models.Model):
    caseno=models.IntegerField(null=True)
    victimip=models.IntegerField(null=True)
    victimaddress = models.IntegerField( null=True)
    maliciousip = models.IntegerField( null=True)    

class auditreport(models.Model):
    file_pdfFile=models.FileField(upload_to="auditreport/",default=None)

class vareport(models.Model):
    file_pdfFile=models.FileField(upload_to="vareport/",default=None)