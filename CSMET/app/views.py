#from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from.forms import *
from .models import * 
from django.shortcuts import render, redirect,reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login




import base64
import io
import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg' before importing pyplot
import matplotlib.pyplot as plt





 





            
   

# Create your views here.
#@login_required(login_url='login')
#def HomePage(request):
 #   return render (request,'home.html')

def DashboardPage(request):
    
    return render (request,'dashboard.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
    
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')


def LoginPage(request):     
    if request.method == 'POST':
        username = request.POST.get('loginuname')
        password = request.POST.get('loginpass1')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
           

    return render(request, 'login.html')


def forgetpPage(request):
     if request.method == 'POST':
        username = request.POST.get('loginuname')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        
        if password1 != password2:
            messages.error(request, "Passwords do not match")
        else:
            try:
                user = User.objects.get(username=username)
                user.set_password(password1)
                user.save()
                messages.success(request, "Password reset successful")
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, "User does not exist")
     return render(request, 'forgetp.html')
            

   
    #return HttpResponseRedirect('/dashboard/')

def LogoutPage(request):
    logout(request)
    return redirect('login')
                                        




def ProjectstrategyPage(request):
    if request.method=="POST":
        projectnumber = request.POST.get('number')
        projectname = request.POST.get('projectname')
        projectiteration = request.POST.get('projectiteration')
        projectlead = request.POST.get('lead')
        estimatedtimeline = request.POST.get('estimatedtimeline')
        automatedvatest = request.POST.get('automatedvatest')
        manualtest = request.POST.get('manualtest')
        performancetest = request.POST.get('performancetest')
       # en=projectStrategy(request, number=projectnumber,  projectname= projectname, projectiteration=projectiteration, lead=projectlead, estimatetimeline=estimatedtimeline, automatedvatest=automatedvatest, manualtest=manualtest, performancetest=performancetest)
        print(projectnumber,projectname,projectiteration,projectlead,estimatedtimeline,automatedvatest,manualtest,performancetest)
        obj = projectStrategy()
        obj.projectnumber = projectnumber
        obj.projectname = projectname
        obj.projectiteration = projectiteration
        obj.projectlead = projectlead
        obj.estimatedtimeline = estimatedtimeline
        obj.automatedvatest = automatedvatest
        obj.manualtest = manualtest
        obj.performancetest = performancetest
        obj.save()
        return redirect('succ')
        # context = {
        
        # }
        # if obj is not None:
        #    messages.success(request, 'Form Successful')
        #    return redirect('va')
        # else:
        #     messages.error(request, "Invalid data. Please try again.")
    return render (request, 'projectstrategy.html')





def ProjectprogressPage(request):
    if request.method=="POST":

        print("Req post")
        print(request.POST)
        projectnumber = request.POST.get('number')
        projectname = request.POST.get('projectname')
        iteration=request.POST.get('iteration')
        startdate=request.POST.get('startdate')
        automatedvatest = request.POST.get('automatedvatest')
        manualtest = request.POST.get('manualtest')
        performancetest = request.POST.get('performancetest')
       
        pn=projectProgress(number=projectnumber,name=projectname,iteration=iteration,startdate=startdate,projectautomatedvatest=automatedvatest,projectmanualtest=manualtest,projectperformancetest=performancetest)
        

        pn.save()
        return redirect('succ')
    #    print(projectnumber,projectnamew,startdatew,automatedvatestw,manualtestw,performancetestw)
        # obj = projectProgress()
        # obj.number = projectnumberw
        # obj.name = projectnamew
        # obj.startdate = startdatew
        # obj.projectautomatedvatest = automatedvatestw
        # obj.projectmanualtest = manualtestw
        # obj.projectperformancetest = performancetes tw
        # obj.save()
    # return HttpResponse('Success')
    return render (request, 'projectprogress.html') 




def ProjectcomplitionPage(request):
     if request.method=="POST":
        print("Req post")
        print(request.POST)
        number=request.POST.get('number')
        name=request.POST.get('name')
        iteration = request.POST.get('iteration')
        startdate = request.POST.get('startdate')
        kn=ProjectComplition(number=number,name=name,iteration=iteration,startdate=startdate)
        kn.save()
        return redirect('succ')
     return render (request,'projectcompletion.html')


def ProjectinductionPage(request):
    if request.method=="POST":
        print("Req post")
        print(request.POST,request.FILES)
        projectname =request.POST.get('projectname')
        projectowner =request.POST.get('projectowner')
        projectnumber=request.POST.get('projectnumber')
        date_projectnumber=request.POST.get('date_projectnumber')
        typeofproject=request.POST.get('typeofproject')
        applicationversion=request.POST.get('applicationversion')
        radio_linkedtopreviousproject=request.POST.get('radio_linkedtopreviousproject')
        radio_avabilityvarepotfromvender=request.POST.get('radio_avabilityvarepotfromvender')
        file_avabilityvarepotfromvender=request.FILES.get('file_avabilityvarepotfromvender')
        file_avabilitysafetohostcertificate=request.FILES.get('file_avabilitysafetohostcertificate')
        radio_avabilitydesignorarchitecturedocumention=request.POST.get('radio_avabilitydesignorarchitecturedocumention')
        file_avabilitydesignorarchitecturedocumention=request.FILES.get('file_avabilitydesignorarchitecturedocumention')
        radio_stagingenvironmentavability=request.POST.get('radio_stagingenvironmentavability')
        radio_ipwhitelisting=request.POST.get('radio_ipwhitelisting')
        sn=projectInduction(projectname=projectname,projectowner=projectowner,projectnumber=projectnumber,date_projectnumber=date_projectnumber,typeofproject=typeofproject,applicationversion=applicationversion,
                 radio_linkedtopreviousproject=radio_linkedtopreviousproject,radio_avabilityvarepotfromvender=radio_avabilityvarepotfromvender,file_avabilityvarepotfromvender=file_avabilityvarepotfromvender,
                 file_avabilitysafetohostcertificate=file_avabilitysafetohostcertificate,
                 radio_avabilitydesignorarchitecturedocumention=radio_avabilitydesignorarchitecturedocumention,file_avabilitydesignorarchitecturedocumention=file_avabilitydesignorarchitecturedocumention,
                 radio_stagingenvironmentavability=radio_stagingenvironmentavability,radio_ipwhitelisting=radio_ipwhitelisting)
        sn.save()
        return redirect('succ')
     
    return render (request,'projectindection.html')


def projectreportPage(request):
    if request.method=="POST":
        print("Req post")
        print(request.POST)
        pronumber=request.POST.get('pronumber')
        proname=request.POST.get('proname')
        proiteration=request.POST.get('proiteration')
        startdate = request.POST.get('startdate')
        enddate=request.POST.get('enddate')
        provadetils=request.POST.get('provadetils')
        proseverit=request.POST.get('proseverit')
        provaparameters=request.POST.get('provaparameters')

        pr=Projectreport(pronumber=pronumber,proname=proname,proiteration=proiteration,startdate=startdate,enddate=enddate,provadetils=provadetils,proseverit=proseverit,provaparameters=provaparameters)
        pr.save()
        return redirect('succ')
    return render(request,'projectreport.html')


def auditinitiationPage(request):
    if request.method=="POST":
        print("Req post")

        print(request.POST)

        projectnumber = request.POST.get('projectnumber')
        unit = request.POST.get('unit')
        station = request.POST.get('station')
        detailsofitassests =request.POST.get('detailsofitassests')
        teamdetails = request.POST.get('teamdetails')
        inititationdate = request.POST.get('inititationdate')

        pks=Auditinitiation(projectnumber=projectnumber,unit=unit,station=station,detailsofitassests=detailsofitassests,teamdetails=teamdetails,inititationdate =inititationdate )
        pks.save()
        return redirect('succ')

    return render(request,'auditinitiation.html')

def auditschedulingPage(request):
    if request.method=="POST":
        print("Req post")
        print(request.POST,request.FILES)
        auditschedulingyear=request.POST.get('auditschedulingyear')
        file_upload=request.FILES.get('file_upload')
        unit=request.POST.get('unit')
        station = request.POST.get('station')
        auditfrom=request.POST.get('auditfrom')
        auditto=request.POST.get('auditto')

        ass=auditscheduling(auditschedulingyear=auditschedulingyear,file_upload=file_upload,unit=unit,station=station,auditfrom=auditfrom,auditto=auditto)
        ass.save()
        return redirect('succ')
   
    return render(request,'auditscheduling.html')

def auditcomplitionPage(request):
    if request.method=="POST":
        print("Req post")
        print(request.POST,request.FILES)
        projectnumber=request.POST.get('projectnumber')
        unit=request.POST.get('unit')
        station = request.POST.get('station')
        initiationdate=request.POST.get('initiationdate')
        complitiondate=request.POST.get('complitiondate')
        file_selectexcelfile=request.FILES.get('file_selectexcelfile')
        file_finalauditreport=request.FILES.get('file_finalauditreport')

        oyy=auditcomplition(projectnumber=projectnumber,unit=unit,station=station,initiationdate=initiationdate,complitiondate=complitiondate,file_selectexcelfile=file_selectexcelfile,file_finalauditreport=file_finalauditreport)
        oyy.save()
        return redirect('succ')

    
    return render(request,'auditcomplition.html')

def auditexecutionPage(request):
     if request.method=="POST":
        print("Req post")
        print(request.POST)
        caseno=request.POST.get('caseno')
        victimip=request.POST.get('victimip')
        victimaddress = request.POST.get('victimaddress')
        maliciousip = request.POST.get('maliciousip')
        kns=auditexecution(caseno=caseno,victimip=victimip,victimaddress=victimaddress,maliciousip=maliciousip)
        kns.save()
        return redirect('succ')
       
 
     return render (request,'auditexecution.html')

def vareportPage(request):
    if request.method=="POST":
        print("Req post")
        print(request.POST,request.FILES)
        file_pdfFile=request.FILES.get('file_pdfFile')
        vare=vareport(file_pdfFile=file_pdfFile)
        vare.save()
        return redirect('succ')
    return render(request,'vareport.html')

def auditreportPage(request):
    if request.method=="POST":
        print("Req post")
        print(request.POST,request.FILES)
        file_pdfFile=request.FILES.get('file_pdfFile')
        rre=auditreport(file_pdfFile=file_pdfFile)
        rre.save()
        return redirect('succ')
    return render(request,'auditreport.html')

def VaPage(request):
    # Line Graph
    plt.figure(figsize=(7, 4))
    plt.title('Project Status')
    qs = PstatusGraph.objects.all()
    x = [x.year for x in qs]
    y = [y.totalnumberofprojectcomplete for y in qs]
    chart = (x, y)
    plt.xticks(rotation=45)
    plt.xlabel('Year')
    plt.ylabel('Total number of Project Complete')
    plt.plot(x, y)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    line_graph = base64.b64encode(image_png).decode('utf-8')

    # Pie Chart
    plt.figure(figsize=(7, 4))
    plt.title('Project Management')
    labels = ['Project Completed', 'Project Under Progress', 'Project Pending', 'Project Ongoing']
    sizes = [20, 40, 10, 30]  
    colors = ['red', 'blue', 'green', 'yellow']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    pie_chart = base64.b64encode(image_png).decode('utf-8')

    # Bar Chart
    plt.figure(figsize=(7, 4))
    plt.title('Project VA Status')
    total_name_of_projects = ['Project A', 'Project B', 'Project C', 'Project D']  # Example project names
    total_va_detected = [50, 30, 40, 20]  # Example total number of VA detected
    plt.bar(total_name_of_projects, total_va_detected)
    plt.xlabel('Total Name of Projects')
    plt.ylabel('Total Number of VA Detected')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    bar_chart = base64.b64encode(image_png).decode('utf-8')

    # Line Chart
    plt.figure(figsize=(7, 4))
    plt.title('Project Complition')
    qs = ProjectcomplitionGraph.objects.all()
    x = [x.priorities for x in qs]
    y = [y.totalnumberofprojectcomparision for y in qs]
    chart = (x, y)
    plt.xticks(rotation=45)
    plt.xlabel('Priorities')
    plt.ylabel('Total number of Project comparision')
    plt.plot(x, y)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    line_chart = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'index1.html', {'line_graph': line_graph, 'pie_chart': pie_chart, 'bar_chart': bar_chart, 'line_chart':line_chart})



def CsPage(request):

     # Pie Chart
    plt.figure(figsize=(7, 4))
    plt.title('Audit Information')
    labels = ['Project Completed', 'Project Under Progress', 'Project Pending', 'Project Ongoing']
    sizes = [20.5, 35.5, 14.8, 29.2]  
    colors = ['#c94ce2', '#b2f33a', '#fb0079', '#eb932e']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    pie_chart = base64.b64encode(image_png).decode('utf-8')

     # Bar Chart
    plt.figure(figsize=(7, 4))
    plt.title('Alerts')
    total_name_of_projects = ['2001', '2002', '2003', '2004','2005', '2006', '2007', '2008']  # Example project names
    total_va_detected = [34, 64, 87, 23, 44, 97, 13, 57]  # Example total number of VA detected
    color = '#89069b'
    plt.bar(total_name_of_projects, total_va_detected, width=0.5,color=color)
    plt.xlabel('Year')
    plt.ylabel('Upcoming Audit')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    bar_chart = base64.b64encode(image_png).decode('utf-8')

    # Bar Chart
    plt.figure(figsize=(7, 4))
    plt.title('Alerts')
    total_name_of_projects1 = ['2001', '2002', '2003', '2004','2005', '2006', '2007', '2008']  # Example project names
    total_va_detected1 = [25, 46, 74, 52, 45, 24, 63, 76]  # Example total number of VA detected
    color = '#5091c6'
    plt.bar(total_name_of_projects1, total_va_detected1 , width=0.5 ,color=color)
    plt.xlabel('Year')
    plt.ylabel('Audit report not receive of ongoing project')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    bar_charts = base64.b64encode(image_png).decode('utf-8')

     # Line Chart
    plt.figure(figsize=(7, 4))
    plt.title('Alerts')
    pa = preauditGraph.objects.all()
    x = [x.year for x in pa]
    y = [y.preauditperpormnotreceived for y in pa]
    chart = (x, y)
    color= '#e1e121'
    plt.xticks(rotation=45)
    plt.xlabel('Year')
    plt.ylabel('Pre-audit perporm not received')
    plt.plot(x, y ,color=color)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    line_chart = base64.b64encode(image_png).decode('utf-8')

    # Line Chart
    plt.figure(figsize=(7, 4))
    plt.title('Alerts')
    skp = quaterlyGraph.objects.all()
    x = [x.year for x in skp]
    y = [y.quaterlyfollowupreportnotreceived for y in skp]
    chart = (x, y)
    color= '#03f533'
    plt.xticks(rotation=45)
    plt.xlabel('Year')
    plt.ylabel('Quaterly follow up report not received')
    plt.plot(x, y ,color=color)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    line_charts = base64.b64encode(image_png).decode('utf-8')

    # Bar Chart
    plt.figure(figsize=(7, 4))
    plt.title('Observation Statistics')
    total_name_of_projects1 = ['Total', 'Resolved', 'Partially resolved', 'Pending']  # Example project names
    total_va_detected1 = [25, 46, 74, 52]  # Example total number of VA detected
    color = '#ea699a'
    plt.bar(total_name_of_projects1, total_va_detected1 , width=0.5 ,color=color)
    plt.xlabel('Categories')
    plt.ylabel('Total number of observations')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    bar_chartss = base64.b64encode(image_png).decode('utf-8')

    # Bar Chart
    plt.figure(figsize=(7, 4))
    plt.title('Observation Risk')
    total_name_of_projects1 = ['High', 'Medium', 'Low', 'Critical' ]  # Example project names
    total_va_detected1 = [25, 46, 74, 52]  # Example total number of VA detected
    color = '#158497'
    plt.bar(total_name_of_projects1, total_va_detected1 , width=0.5, color=color)
    plt.xlabel('Categories')
    plt.ylabel('Total number of observations')
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    bar_chartsss = base64.b64encode(image_png).decode('utf-8')


    return render (request,'index2.html', {'pie_chart': pie_chart, 'bar_chart': bar_chart, 'bar_charts': bar_charts, 'line_chart':line_chart, 'line_charts':line_charts, 'bar_chartss': bar_chartss, 'bar_chartsss': bar_chartsss})



def SuccPage(request):
    return render(request,'success.html')