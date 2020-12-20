#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:45:11 2020

@author: louisbard


"""

from filtrage import *
import random 
from voisinage import *

def gen_weights(z):
    
    # z : number of scalarization
    # Q = 2 objectives
    # m = z+1
    
    res = []
    
    for i in range(z+1):
        
        x=i/z
        
        res.append((x,abs(1-x)))
        
    return res



def fitness(sol,w,instance):
    
    s = evaluation(instance,sol)
    
    r = s[0]*w[0]+s[1]*w[1]
    
    return r

def k_opt(S):
    
    L=list(S)
    
    i=0
    
    while(i<=2):
        
        m = random.choice(range(len(L)))
        
        n = random.choice(range(len(L)))
        
        L[m],L[n]=L[n],L[m]
        
        i=i+1
        
    return L



        



def restart_search(z,P,instance):
    
    # z : number of scalarizations
    
    # N : neighbordhood structure
    
    # P : search length 
    
    w = gen_weights(z)
    
    archive = []
    
    for x in w :
        
        s = gen_sol()
        
        sprime = ILS(s,P,fitness,x,instance)
        
        archive.append(sprime)
        
    #print(archive)
    
    
        
    l=off_line(instance,archive)
    
    print("prout")
    
    return l
        

# PROBLEME AVEC LA FITNESS / A RELIRE 



def ILS(s0,P,fitness,w,instance):
    
    
    
    s = HillClimbing(s0, fitness, w, instance)
    
    k=0
    
    while(k<=P):
        
        
        
        
        sprime = k_opt(s)
        
        setoile = HillClimbing(sprime, fitness,w, instance)
        
        if fitness(setoile,w,instance)<fitness(s,w,instance):
            
            s=setoile
            
            
            
        
        print("p=",k)
        
        k=k+1
    
    return s 


def HillClimbing(s0,fitness,w,instance):
    
    
    
    
    k=0
    
    while(k<=10):
        
       S = generate(s0,10)
       
     
                
      
       
       for s in S : 
           
        
        
           if fitness(s,w,instance)<fitness(s0,w,instance):
              s0=s
              
             # print(fitness(s0,w,instance))
                   
         
      
    
       
       k=k+1
       
    return s0

#instance a_b

A_a_e_2 = []

for i in range(5):
    
    A_a_e_2.append(restart_search(100,50,a_b))
    
A_a_f_2 = []

for i in range(5):
    
    A_a_f_2.append(restart_search(100,100,a_b))
    
#instance c_d

B_a_e_2 = restart_search(100,50,c_d)


    
B_a_f_2 = restart_search(100,100,c_d)



C_a_e_2 = restart_search(100,50,e_f)


C_a_f_2 = restart_search(100,100,e_f)




        

        
    
    
        
        
        
        