#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:52:18 2020

@author: louisbard
"""
import numpy as np
import random
import time


import matplotlib.pyplot as plt 

gen = np.genfromtxt("randomA100.txt",skip_header=7)


def gen_instance(file1,file2):
    
    A = np.zeros((100,100),dtype='i,i')
   
    p = 0
    
    gen1 = np.genfromtxt(file1,skip_header=7)
    
    gen2 = np.genfromtxt(file2,skip_header=7)
    
    p = 0
    
    for i in range(100):
        
        for j in range(i,100):
            
            A[i,j]=(gen1[p],gen2[p])
            A[j,i]=(gen1[p],gen2[p])
            p=p+1
    
    return A 

a_b = gen_instance("randomA100.txt","randomB100.txt")
c_d = gen_instance("randomC100.txt","randomD100.txt")
e_f = gen_instance("randomE100.txt","randomF100.txt")

            

def evaluation(instance,sol):
    
    res = [0,0]
    
    for i in range(len(sol)-1):
        
        res[0] += instance[ sol[i],sol[i+1] ][0]
        
        res[1] += instance[ sol[i],sol[i+1] ] [1]
                    
    res[0] += instance[ sol[0],sol[len(sol)-1] ][0]
    
    res[1] += instance[ sol[0],sol[len(sol)-1] ][1]
    
    return res


def gen_sol():
    l = random.sample(range(100), 100)
    return l


def dominance(E, etiq):
    verif = []
    if etiq == [] :
        return False 
    else : 
        for ele in etiq:
            if (ele[0] <= E[0] and ele[1] <= E[1] and (ele[0] < E[0] or ele[1] < E[1])):
                    verif.append('dominé')
    return('dominé' in verif)

def mise_a_jour(liste):
    gr=[]
    for ele in liste:
        if not dominance(ele, liste):
            gr.append(ele)
    return(gr)


def off_line(instance,solutions):
    
    S=[]
    
    for i in range(len(solutions)):
        
        ev = evaluation(instance,solutions[i])
        
        S.append(evaluation(instance,solutions[i]))
        
        
        
        plt.scatter(ev[0],ev[1], c="red")
        
    l=mise_a_jour(S)
    
    for x in l :
        plt.scatter(x[0],x[1],c="yellow")
    
    return l


def on_line(x,archive,instance):
    ev = evaluation(instance,x)
   # plt.scatter(ev[0],ev[1], c="red")
    archive.append(ev)
    l=mise_a_jour(archive)
    return l 

#on_line
   

    
   
    
    
        
        
    
    
    
    
    
   
    
    
    
            


