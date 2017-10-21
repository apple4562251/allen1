# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scipy.io import loadmat
from pandas import Series
import os
from math import exp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol,symbols,solve
from random import randint
from scipy import stats
from scipy.sparse import coo_matrix
from scipy.optimize import fsolve
from sympy import solve_poly_system
from sympy import Function, rsolve

"""一個找出這SYDER的路徑
print(os.getcwd()) """
"""     讀檔   """
X=loadmat('5_X.mat')
T=loadmat('5_T.mat')
"""------------"""  

X1=X['X']
T1=T['T']
X1=np.array(X1)
T1=np.array(T1)
"""----------轉置-------------"""
def matrix(t,xj):
  """10*20"""
  o=np.vstack(xj)
  """20*10"""
  ot=np.vstack(xj).transpose()
  """----------wML的計算---------"""
  w=np.dot(np.dot(np.linalg.pinv(np.dot(ot,o)),ot),t)
  return w

"""----------y(x,w)方程式--------------"""
def summation(x,w):
  num=0
  for m in range(0,4):
    num=num+w[m+1]*x[m]
  num=num+w[0]
  return num
"""------------M=1-------------"""  
"""------------算o矩陣----------"""
design1=[]
p1=[]
p2=[]
for k in range(0,150):
   p=[1]
   pp=[]
   for i in range(0,4):
      p.append(X1[k][i])
      pp.append(X1[k][i])
   if k<40 or 49<k<90 or 99<k<140:
      design1.append(p)
      p1.append(pp)
   if 39<k<50 or 89<k<100 or 139<k<150:
      p2.append(pp) 
design1=np.array(design1)
p1=np.array(p1)
p2=np.array(p2)
t1=[]
t2=[]
for k in range(0,150):
   if k<40 or 49<k<90 or 99<k<140:
      t1.append(T1[k])
   if 39<k<50 or 89<k<100 or 139<k<150:
      t2.append(T1[k])
t1=np.array(t1)
t2=np.array(t2)   
"""------------------"""
w1=matrix(t1,design1)
def M1(h,e,p,t): 
  error=0
  for i in range(h,e): 
    error=error+(summation(p[i],w1)-t[i])**2
  error_rms=np.sqrt(error/(e-h))
  return error_rms
print("-----M=1------")
print(M1(0,120,p1,t1))
print(M1(0,30,p2,t2))
"""---------M=2------------"""
design2=[]
p3=[]
p4=[]
for k in range(0,150):
   pp=[1]
   ppp=[]
   for i in range(0,4):
      pp.append(X1[k][i])
      ppp.append(X1[k][i])
   for j in range(0,4):
      for i in range(0,4):
        num=X1[k][j]*X1[k][i]
        pp.append(num)
        ppp.append(num)
   if k<40 or 49<k<90 or 99<k<140:
      design2.append(pp)
      p3.append(ppp)
   if 39<k<50 or 89<k<100 or 139<k<150:
      p4.append(ppp)
design2=np.array(design2)
p3=np.array(p3)
p4=np.array(p4)
def summation2(x,w):
  num=0
  for m in range(0,4):
    q=5
    num=num+w[m+1]*x[m]
  for j in range(0,4):
    for i in range(0,4):
      num=num+w[q]*x[j]*x[i]  
      q=q+1
  num=num+w[0]
  return num    
"""--------error function---------"""
w2=matrix(t1,design2)
def M2(h,e,p,t): 
  error2=0
  for i in range(h,e): 
    error2=error2+(summation2(p[i],w2)-t[i])**2
  error_rms=np.sqrt(error2/(e-h))
  return error_rms
print("-----M=2------")
print(M2(0,120,p3,t1))
print(M2(0,30,p4,t2))
"""------------------------"""
print("**************")
def summation3(x,w):
  num=0
  for m in range(0,3):
    q=4
    num=num+w[m+1]*x[m]
  for j in range(0,3):
    for i in range(0,3):
      num=num+w[q]*x[j]*x[i]  
      q=q+1
  num=num+w[0]
  return num   
def M3(h,e,p,t,w): 
  error2=0
  for i in range(h,e): 
    error2=error2+(summation3(p[i],w)-t[i])**2
  error_rms=np.sqrt(error2/(e-h))
  return error_rms
p5=[]
p6=[]
p7=[]
p8=[]
p9=[]
p10=[]
p11=[]
p12=[]
design3=[]
design4=[]
design5=[]
design6=[]
num=0
num1=0
num2=0
num3=0
for k in range(0,150):
   pp=[]
   ppp=[1]
   
   """----------0,1,2---------------"""
   for i in (0,1,2):
      pp.append(X1[k][i])
      ppp.append(X1[k][i])
   for j in (0,1,2):
      for i in (0,1,2):
        num=X1[k][j]*X1[k][i]
        ppp.append(num)
   if k<40 or 49<k<90 or 99<k<140:
      p5.append(pp)
      design3.append(ppp)
   if 39<k<50 or 89<k<100 or 139<k<150:
      p6.append(pp) 

   """----------0,2,3---------------"""
   pp1=[]
   ppp1=[1]
   for i in (0,2,3):
      pp1.append(X1[k][i])
      ppp1.append(X1[k][i])
   for j in (0,2,3):
      for i in (0,2,3):
        num1=X1[k][j]*X1[k][i]
        ppp1.append(num1)
   if k<40 or 49<k<90 or 99<k<140:
      p7.append(pp1)
      design4.append(ppp1)
   if 39<k<50 or 89<k<100 or 139<k<150:
      p8.append(pp1) 

   """----------0,1,3---------------"""
   pp2=[]
   ppp2=[1]
   for i in (0,1,3):
      pp2.append(X1[k][i])
      ppp2.append(X1[k][i])
   for j in (0,1,3):
      for i in (0,1,3):
        num2=X1[k][j]*X1[k][i]
        ppp2.append(num2)
   if k<40 or 49<k<90 or 99<k<140:
      p9.append(pp2)
      design5.append(ppp2)
   if 39<k<50 or 89<k<100 or 139<k<150:
      p10.append(pp2) 

   """----------1,2,3---------------"""
   pp3=[]
   ppp3=[1]
   for i in (1,2,3):
      pp3.append(X1[k][i])
      ppp3.append(X1[k][i])
   for j in (1,2,3):
      for i in (1,2,3):
        num3=X1[k][j]*X1[k][i]
        ppp3.append(num3)
   if k<40 or 49<k<90 or 99<k<140:
      p11.append(pp3)
      design6.append(ppp3)
   if 39<k<50 or 89<k<100 or 139<k<150:
      p12.append(pp3) 

p5=np.array(p5)
p6=np.array(p6)
p7=np.array(p7)
p8=np.array(p8)
p9=np.array(p9)
p10=np.array(p10)
p11=np.array(p11)
p12=np.array(p12)
design3=np.array(design3)
design4=np.array(design4)
design5=np.array(design5)
design6=np.array(design6)
print("(0,1,2)")
w3=matrix(t1,design3)
print(M3(0,120,p5,t1,w3))
print(M3(0,30,p6,t2,w3))
print("(0,2,3)")
w4=matrix(t1,design4)
print(M3(0,120,p7,t1,w4))
print(M3(0,30,p8,t2,w4))
print("(0,1,3)")
w5=matrix(t1,design5)
print(M3(0,120,p9,t1,w5))
print(M3(0,30,p10,t2,w5))
print("(1,2,3)")      
w6=matrix(t1,design6)
print(M3(0,120,p11,t1,w6))
print(M3(0,30,p12,t2,w6))
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      