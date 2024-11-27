from django import forms                 
from. models import projectStrategy,projectProgress

class FirstForm(forms.Form):
    

    number = forms.IntegerField()
    projectname = forms.CharField(max_length=80 )
    projectiteration =forms.CharField(max_length=80)
    estimatetimeline = forms.DateTimeField()
    lead = forms.CharField(max_length=80)
    automatedvatest = forms.CharField()
    manualtest = forms.CharField()
    performancetest = forms.CharField()

    
class SecondForm(forms.Form):
    
    number = forms.IntegerField()
    name=forms.CharField(max_length=8)
    iteration = forms.CharField(max_length=80)
   # fk = models.ForeignKey(projectStrategy, on_delete=models.CASCADE)
    startdate = forms.DateTimeField()
    projectautomatedvatest = forms.CharField()
    projectmanualtest = forms.CharField()
    projectperformancetest = forms.CharField()

class ThirdForm(forms.Form):
    projectname =forms.CharField(max_length=80)
    projectowner =forms.CharField(max_length=80)
    projectnumber=forms.IntegerField()
    date_projectnumber=forms.DateTimeField()
    typeofproject=forms.CharField()
    applicationversion=forms.CharField()
    radio_linkedtopreviousproject=forms.CharField()
    radio_avabilityvarepotfromvender=forms.CharField()
    file_avabilityvarepotfromvender=forms.FileField()
   
    file_avabilitysafetohostcertificate=forms.FileField()
    radio_avabilitydesignorarchitecturedocumention=forms.CharField()
    file_avabilitydesignorarchitecturedocumention=forms.FileField()
    radio_stagingenvironmentavability=forms.CharField()
    radio_ipwhitelisting=forms.CharField()

class FourthForm(forms.Form):
    number=forms.IntegerField()
    name=forms.CharField(max_length=80)
    iteration = forms.CharField(max_length=80)
    startdate = forms.DateTimeField()

class fifthForm(forms.Form):
    pronumber=forms.IntegerField()
    proname=forms.CharField(max_length=80)
    proiteration = forms.CharField(max_length=80)
    startdate = forms.DateTimeField()
    enddate=forms.DateField()
    provadetils=forms.CharField(max_length=80)
    proseverit=forms.CharField(max_length=80)
    provaparameters=forms.CharField(max_length=80)

class sixthForm(forms.Form):
    projectnumber = forms.IntegerField() 
    unit = forms.CharField(max_length=80)
    station = forms.CharField(max_length=80)
    detailsofitassests = forms.CharField(max_length=80)
    teamdetails = forms.CharField(max_length=80)
    inititationdate = forms.DateTimeField()

class sevenForm(forms.Form):
    auditschedulingyear=forms.IntegerField()
    file_upload=forms.FileField()
    unit=forms.CharField(max_length=80)
    station=forms.CharField(max_length=80)
    auditfrom=forms.DateField()
    auditto=forms.DateField()    

class eightForm(forms.Form):
    projectnumber = forms.IntegerField()
    unit = forms.CharField(max_length=80)
    station=forms.CharField(max_length=80)
    initiationdate=forms.DateField()
    complitiondate=forms.DateField() 
    file_selectexcelfile=forms.FileField()    
    file_finalauditreport=forms.FileField()    

class nineForm(forms.Form):
    caseno=forms.IntegerField()
    victimip=forms.IntegerField()
    victimaddress = forms.IntegerField()
    maliciousip = forms.IntegerField()   

class tenForm(forms.Form):
    file_pdfFile=forms.FileField()

class elevenForm(forms.Form):
    file_pdfFile=forms.FileField() 