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
p1=[]
for k in range(0,150):
   p=[1]
   for i in range(0,4):
      p.append(X1[k][i])
   p1.append(p)
"""---------class----------"""
o=np.vstack(p1[0:40])
ot=np.vstack(p1[0:40]).transpose()
t=T1[0:40]
e=np.dot(ot,t)
w=np.dot(ot,o)

h=np.eye(5)
print(np.linalg.inv(w))

"""--------error function---------"""
w1=matrix(T1[0:40],p1[0:40])
w2=matrix(T1[50:90],p1[50:90])
w3=matrix(T1[100:140],p1[100:140])
def M1(h,e,w): 
  error=0
  for i in range(h,e): 
    error=error+(summation(p1[i],w)-T1[i])**2
  error_rms=np.sqrt(error/(e-h))
  return error_rms
print("[M=1]")  
print("Iris Setosa(class 1)")
print("training set",M1(0,40,w1))
print("test set ",M1(40,50,w1))
print("--------------------")
print("Iris Versicolour(class 2)")
print("training set",M1(50,90,w2))
print("test set ",M1(90,100,w2))
print("--------------------")
print("Iris Virginica(class 3)")
print("training set",M1(100,140,w3))
print("test set ",M1(140,150,w3))



"""------------M=2-------------"""  
"""------------算o矩陣----------"""
p2=[]
w2=[]
for k in range(0,150):
   pp=[1]
   for i in range(0,4):
      pp.append(X1[k][i])
   for j in range(0,4):
      for i in range(0,4):
        num=X1[k][j]*X1[k][i]
        pp.append(num)
   p2.append(pp) 
def matrix2(t,xj):
  """10*20"""
  o=np.vstack(xj)
  """20*10"""
  ot=np.vstack(xj).transpose()
  """----------wML的計算---------"""
  w=np.dot(np.dot(np.linalg.pinv(np.dot(ot,o)),ot),t)  
  return w
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
w4=matrix2(T1[0:40],p2[0:40])
w5=matrix2(T1[50:90],p2[50:90])
w6=matrix2(T1[100:140],p2[100:140])
def M2(h,e,w): 
  error2=0
  for i in range(h,e): 
    error2=error2+(summation(p2[i],w)-T1[i])**2
  error_rms=np.sqrt(error2/(e-h))
  return error_rms
print("[M=2]")  
print("Iris Setosa(class 1)")
print("training set",M2(0,40,w4))
print("test set ",M2(40,50,w4))
print("--------------------")
print("Iris Versicolour(class 2)")
print("training set",M2(50,90,w5))
print("test set ",M2(90,100,w5))
print("--------------------")
print("Iris Virginica(class 3)")
print("training set",M2(100,140,w6))
print("test set ",M2(140,150,w6))
    

"""----------5-2小題---------------"""
p3=[]
p4=[]
p5=[]
p6=[]
w2=[]
for k in range(0,150):
   pp=[1]
   """----------0,1,2---------------"""
   for i in (0,1,2):
      pp.append(X1[k][i])
   for j in range(0,4):
      for i in range(0,4):
        num=X1[k][j]*X1[k][i]
        pp.append(num)
   p3.append(pp) 
   """----------0,2,3---------------"""
   pp=[1]
   for i in (0,2,3):
      pp.append(X1[k][i])
   for j in range(0,4):
      for i in range(0,4):
        num=X1[k][j]*X1[k][i]
        pp.append(num)
   p4.append(pp) 
   """----------0,1,3---------------"""
   pp=[1]
   for i in (0,1,3):
      pp.append(X1[k][i])
   for j in range(0,4):
      for i in range(0,4):
        num=X1[k][j]*X1[k][i]
        pp.append(num)
   p5.append(pp) 
   """----------1,2,3---------------"""
   pp=[1]
   for i in (1,2,3):
      pp.append(X1[k][i])
   for j in range(0,4):
      for i in range(0,4):
        num=X1[k][j]*X1[k][i]
        pp.append(num)
   p6.append(pp) 

def matrix3(t,xj):
  """10*20"""
  o=np.vstack(xj)
  """20*10"""
  ot=np.vstack(xj).transpose()
  """----------wML的計算---------"""
  w=np.dot(np.dot(np.linalg.pinv(np.dot(ot,o)),ot),t)  
  return w
def summation3(x,w):
  num=0
  for m in range(0,3):
    q=5
    num=num+w[m+1]*x[m]
    for j in range(0,3):
      for i in range(0,3):
         num=num+w[q]*x[j]*x[i]  
         q=q+1
  num=num+w[0]
  return num    


def M3(h,e,w,p): 
  error2=0
  for i in range(h,e): 
    error2=error2+(summation3(p[i],w)-T1[i])**2
  error_rms=np.sqrt(error2/(e-h))
  return error_rms
print("5-2[M=2]")  
print("Iris Setosa(class 1)")
print("(0,1,2)")
w7=matrix3(T1[0:40],p3[0:40])
print("training set",M3(0,40,w7,p3))
print("(0,2,3)")
w7=matrix3(T1[0:40],p4[0:40])
print("training set",M3(0,40,w7,p4))
print("(0,1,3)")
w7=matrix3(T1[0:40],p5[0:40])
print("training set",M3(0,40,w7,p5))
print("(1,2,3)")
w7=matrix3(T1[0:40],p6[0:40])
print("training set",M3(0,40,w7,p6))
"""--------------------------"""
print("Iris Versicolour(class 2)")
print("(0,1,2)")
w7=matrix3(T1[50:90],p3[50:90])
print("training set",M3(50,90,w7,p3))
print("(0,2,3)")
w7=matrix3(T1[50:90],p4[50:90])
print("training set",M3(50,90,w7,p4))
print("(0,1,3)")
w7=matrix3(T1[50:90],p5[50:90])
print("training set",M3(50,90,w7,p5))
print("(1,2,3)")
w7=matrix3(T1[50:90],p6[50:90])
print("training set",M3(50,90,w7,p6))   
print("Iris Virginica(class 3)")
print("Iris Setosa(class 1)")
print("(0,1,2)")
w7=matrix3(T1[100:140],p3[100:140])
print("training set",M3(100,140,w7,p3))
print("(0,2,3)")
w7=matrix3(T1[100:140],p4[100:140])
print("training set",M3(100,140,w7,p4))
print("(0,1,3)")
w7=matrix3(T1[100:140],p5[100:140])
print("training set",M3(100,140,w7,p5))
print("(1,2,3)")
w7=matrix3(T1[100:140],p6[100:140])
print("training set",M3(100,140,w7,p6))     


    
