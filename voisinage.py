#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:44:38 2020

@author: louisbard


"""


import random


def swap(Q,i,j):

    L=list(Q)
    L[i],L[j]=L[j],L[i]
    
    return L

def echange(Q,j):
    
    L=list(Q)
    
    L[j],L[j+1]=L[j+1],L[j]
    
    return L



def generate(L,k):
    
    
    p=0
    
    S=[]
    
    while(p<=k):
        
        
    
        
            
        i = random.choice(range(len(L)-1))
            
            
            
        P = echange(L,i)
                
        S.append(P)
            
        p=p+1
        
    return S
    

                
