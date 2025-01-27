# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:02:25 2021

@author: duwat
"""
import numpy as np




def overdrive_1(x,drive,fc1,fc2,ass):
    n=len(x)
    #filtre passe bas
    fc=1/fc1
    inputfpb_data= x
    
    for i in range(1,n):
        x[i]= fc*x[i-1]+inputfpb_data[i]
        
    ##filtre passe haut
    fc=-1/fc2
    inputfpb_data= x
    
    for i in range(1,n):
        x[i]= fc*x[i-1]+inputfpb_data[i]
        
       
    for i in range (n):
        x[i]=x[i]+ ass
        a=np.sin(((drive+1)/101)*(np.pi/2))
        k=2*a/(1-a)
        l=x[i]
        j=np.absolute(l)
        if drive==0:
            x[i]=x[i] - ass
        elif l==0:
            x[i]=0 - ass
        else:
            x[i]=((1+k)*l)/(1+k*j)+l - ass
    x = 0.99 * x / max(abs(x))
    print(max(x))
    return x




def overdrive_2(x,gain,ass):  
    n=len(x)          
    for i in range (n):
        x[i]=x[i]*gain-ass
        j=np.absolute(x[i])  
        
        if j<1/3:
            x[i]=2*x[i]+ass
            
        elif 1/3<x[i]<2/3:
            
            x[i]=(3-((2-3* x[i])**2))/3+ass
            
        elif -2/3<x[i]<-1/3:
            x[i]=-((3+ass-((2-ass-3* (-x[i]))**2))/3)
        elif x[i]<-2/3:
            x[i]=-1+ass
            
        else:
            x[i]=1+ass
    

    return x