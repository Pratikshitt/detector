from django.shortcuts import render,redirect
from django.http import HttpResponse
from firstapp.models import topic,webpage,ModelForm,MyModel,GeneralRemedies,AuyervedicRemedies,HomeopathicRemedies,ip
from . import forms
import datetime
# from dateutil import relativedelta


from myproject import fake_model

# Create your views here.

#def index(request):
 #   return HttpResponse("Hello World")

def index(request):
    mydict={'insert_me':"Hello i am in pratik"}
    return render(request,'index.html',context=mydict)

def first(request):
   # listt = topic.objects.all
   # print(listt)
    #myweb={"list":"listt"}
    # x,y=get_client_ip(request)
    # print(x)
    # print(y)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ipaddress = x_forwarded_for.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')
    get_ip= ip() 
    if ip.objects.exists():
        l='.'.join(ipaddress.split('.')[0:-2]) 
        print(l)
        
        x=(ip.objects.filter(ip_address=ipaddress).exists())
        get_ip= ip.objects.get(ip_address=ipaddress)
        y='.'.join(get_ip.ip_address.split('.')[0:-2]) 
       
        print(x)
        print(y)
        print(y==l)
        if (x and (y==l)):
            get_ip= ip.objects.get(ip_address=ipaddress)
            print(get_ip.pub_date)
            print('Already there')
    #import datetime
        else:
            get_ip.ip_address= ipaddress
            get_ip.pub_date = datetime.date.today()
            get_ip.save()
    else:
        get_ip.ip_address= ipaddress
        get_ip.pub_date = datetime.date.today()
        get_ip.save()
    

        
    #imported class from model
    
    
    
    if request.method=="POST":
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')
        print(request.POST.get('Contact'))
        get_ip= ip.objects.get(ip_address=ipaddress)
        if request.POST.get("Predict"):
           
            
            if ip.objects.filter(ip_address=ipaddress).exists():
                get_ip= ip.objects.get(ip_address=ipaddress)
                x=datetime.date.today()
                print(x.day)
                
                y=get_ip.pub_date
                print(y.day)
                # date_format = "%H:%M:%S"
                # time_start = str(get_ip.pub_date)
                # time_end = str(instance.datetime.date.today())

     # Now to get the time difference.
                # diff = datetime.strptime(time_end, date_format) - datetime.strptime(time_start, date_format)

     # Get the time in hours i.e. 9.60, 8.5
                result =x.day-y.day
                if(result>3):

                    return HttpResponse("PLs Visit Doctor asap")
                else:
                    return redirect('/form')
            else:
                return 1      

            
            
        if request.POST.get("Contact"):
            return redirect('/contact')
    return render(request,'firstt.html')    

def form_name_view(request):
   # form=forms.FormName()
        
   # try:
        form=forms.MyModel()
        if request.method=="POST":
            form=forms.MyModel(request.POST)
            if form.is_valid():
                
                form.save(commit=True)
                some_var = form.cleaned_data.get('Symptoms')
                days=form.cleaned_data.get('Days')
                print(days)
                print(some_var)
                for i in range(0, len(some_var)): 
                    some_var[i] = int(some_var[i])
                mydict={}
                li=[]
                for i in range(1,32):
                    if(i in some_var):
                        mydict[i]=True
                        li.append(1)
                    else:
                        mydict[i]=False
                        li.append(0)
                print(mydict) 
                print(li) 
                l=li           
                prediction=fake_model.fake_predict(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15],l[16],l[17],l[18],l[19],l[20],l[21],l[22],l[23],l[24],l[25],l[26],l[27],l[28],l[29])
                request.session['prediction']=prediction
                if request.POST.get('SUBMIT'):
                    if days>3:
                        return redirect('/disease') 
                    else:
                        return HttpResponse("Wait for some more time")   

                 
                returnbutton= request.POST.get('Back')
                print(returnbutton)
                if returnbutton:
                   return redirect('/index')
  
                #return redirect('/disease')     
                #listt=[]
                #for i in range(1,4):
                 #   if(mydict[i].values()):
                  #      listt=1
                   # else:
                    #    listt=0
                        
                #print(listt)
               # return render(request,'form.html',{'form':form})   
   

        
    
        return render(request,'form.html',{'form':form})  
  #  except:
    #    print("Exception occured")  


def disease(request):
    prediction = request.session['prediction']
    print(prediction)
    if request.method=="POST":
        if request.POST.get("Back"):
            return redirect('/form')
        data=GeneralRemedies.objects.filter(Diseasename=prediction)[0]
        Adata=AuyervedicRemedies.objects.filter(Diseasenam=prediction)[0]
        print(data.Diseasename)
        data_list=data.Remedies.split(r'\n')

        # print(data_list)
       
        if request.POST.get('GeneralRemedies'):
            return redirect('/remedy')
        if request.POST.get('AuyervedicRemedies'):
            return redirect('/Aremedy')
        if request.POST.get('HomeopathicRemedies'):
            return redirect('/Hremedy')    
        
        
    else:
         
        return render(request,'result.html',{'prediction':prediction})  


def contact(request):
    if request.method=="POST":
        returnbutton= request.POST.get('Back')
               
        if returnbutton:
            return redirect('/index')
    return render(request,'contact.html')


def remedy(request):
    prediction = request.session['prediction']
    data=GeneralRemedies.objects.filter(Diseasename=prediction)[0]
    print(data.Diseasename)
    data_list=data.Remedies.split(r'\n')
    
    if request.method=="POST":
        if(request.POST.get("Back")):
            return redirect('/disease')    
    return render(request,'remedy.html',{'data':data,'data_list':data_list})  


def Aremedy(request):
    prediction = request.session['prediction']
    Adata=AuyervedicRemedies.objects.filter( Diseasenam=prediction)[0]
    
    data_list=Adata.Remedie.split(r'\n')
    
    if request.method=="POST":
        if(request.POST.get("Back")):
            return redirect('/disease')    
    return render(request,'Aremedy.html',{'Adata':Adata,'data_list':data_list})
def Hremedy(request):
    prediction = request.session['prediction']
    Hdata=HomeopathicRemedies.objects.filter( Diseasena=prediction)[0]
    
    data_list=Hdata.Remedi.split(r'\n')
    
    if request.method=="POST":
        if(request.POST.get("Back")):
            return redirect('/disease')    
    return render(request,'Hremedy.html',{'Adata':Hdata,'data_list':data_list})   

# def my_post_view(request, post_id):
#     #you could check for logged in users as well.
#     created = TrackedPosts.objects.get_or_create( ip=request.ip)
#     print(created) #note, not actual api
#     if created:
#         created.post.count += 1
#         created.post.save()
#     return 1         

# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#         ip.pub_date = datetime.date.today() 
#     return ip,ip.pub_date

    
                                      
    
