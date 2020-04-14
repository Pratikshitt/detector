from django.shortcuts import render,redirect
from django.http import HttpResponse
from firstapp.models import topic,webpage,ModelForm,MyModel,GeneralRemedies,AuyervedicRemedies
from . import forms
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
    if request.method=="POST":
        print(request.POST.get('Contact'))
        if request.POST.get("Predict"):
            return redirect('/form')
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

    
                                      
    
