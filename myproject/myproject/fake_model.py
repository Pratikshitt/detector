import csv
def fake_predict(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae):
    import pickle
    x=[[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae]]
    randomforest=pickle.load(open('myproject/model.sav','rb'))
    prediction=randomforest.predict(x)
    if y==1:
        prediction='Rabies'
    elif u==1:
        prediction='Chicken Pox'
    elif o==1:
        prediction="Measales"
    elif ad==1:
        prediction="Conjuctivities"    
    elif prediction==1:
        prediction="Anaemia"
    elif prediction==2:
        prediction="Asthma"    
    elif prediction==5:
        prediction="Common Cold" 
    elif prediction==12:
        prediction="Diarrohea"       
    elif prediction==7:
        prediction="FLU" 
    elif prediction==13:
        prediction="Hepatatis A" 
    elif prediction==14:
        prediction="Malaria" 
    elif prediction==9:
        prediction="Measales" 
    elif prediction==11:
        prediction="TB" 
    elif prediction==15:
        prediction="Typhoid" 
    elif prediction==8:
        prediction="Influenza" 
    elif prediction==4:
        prediction="Cholera" 
    else:
        prediction="AIDS"                                          
    return prediction
