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
df = pd.read_csv('4_train.csv')
dt = pd.read_csv('4_test.csv')
X=loadmat('5_X.mat')
T=loadmat('5_T.mat')
"""------------"""  
x=np.array(df.x)
t=np.array(df.t)
x2=np.array(dt.x)
t2=np.array(dt.t)
X1=X['X']
T1=T['T']
"""-----------o矩陣-----------"""
def x_arr(M):
   x_arr=[]
   for m in range(0,M):
     x_arr.append(X1[m])
   return np.vstack(x_arr)
def x_arr2(M):
   x_arr2=[]
   for m in range(0,M+1):
     x_arr2.append(np.power(x2,m))
   return x_arr2
"""----------轉置-------------"""
def matrix(t,xj):
  """10*20"""
  o=np.vstack(xj)
  """20*10"""
  ot=np.vstack(xj).transpose()
  """----------wML的計算---------"""
  w=np.dot(np.dot(np.linalg.inv(np.dot(ot,o)),ot),t)
  return w

"""----------y(x,w)方程式--------------"""
def summation(x,w):
  num=0
  for m in range(0,4):
    num=num+w[m]+w[m+1]*x[m]
  return num
"""------------M=1-------------"""  
"""------------算o矩陣----------"""
p1=[]
for k in range(0,150):
   p=[1]
   for i in range(0,4):
      p.append(float(X1[k][i]))
   p1.append(p)
"""---------class----------"""
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
   p=[1]
   for i in range(0,4):
      p.append(float(X1[k][i]))
   for j in range(0,4):
      for i in range(0,4):
        num=X1[k][j]*X1[k][i]
        p.append(num)
   p2.append(p) 
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
    num=num+w[m]+w[m+1]*x[m]
    for j in range(0,4):
      for i in range(0,4):
         num=num+w[q]*x[j]*x[i]  
         q=q+1
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
    
    
    
    
