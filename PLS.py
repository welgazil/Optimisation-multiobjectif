#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:12:13 2020

@author: louisbard
"""

import random

from voisinage import * 

from filtrage import *

def PLS(A_0,instance):
    
    explored={}
    
    for x in A_0:
        
        explored[str(id(x))]=False
        
    A=list(A_0)
    
    while (len(A_0)!=0):
        
        x = random.choice(A_0)
        
        print("1")
        
        S = generate(x,100)
        
        for x_p in S :
            
            f = evaluation(instance,x_p)
            
            if not dominance(f, A):
                
                A=on_line_2(x_p,A,instance)
                
       
                    
        
        explored[str(id(x))] = True
        
        A_0 = [x for x in A if explored[str(id(x))]==False]
        
    return A
            
            
def on_line_2(x,archive,instance):
     
    
    archive.append(ev)
    l=mise_a_jour_2(archive)
    return l 


def mise_a_jour_2(liste,instance):
    gr=[]
    
    liste2 = [evaluation(instance,x) for x in liste]
    
    for ele in liste:
        
        
        
        a = evaluation(instance,ele)
        
        if not dominance(a, liste2):
            gr.append(ele)
    return(gr)           
        
        
        
        
    
    
        
        