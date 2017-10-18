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

"""一個找出這SYDER的路徑
print(os.getcwd()) """
"""     讀檔   """
df = pd.read_csv('4_train.csv')
dt = pd.read_csv('4_test.csv')
X=loadmat('5_X')
T=loadmat('5_T')
"""------------"""  
x=np.array(df.x)
t=np.array(df.t)
x2=np.array(dt.x)
t2=np.array(dt.t)
"""-----------o矩陣-----------"""
def x_arr(x,M):
   x_arr=[]
   for m in range(0,M+1):
     x_arr.append(np.power(x,m))
   return x_arr
"""----------轉置-------------"""
def matrix(t,xj):
  """10*20"""
  ot=np.vstack(xj)
  """20*10"""
  o=np.vstack(xj).transpose()
  """----------wML的計算---------"""
  w=np.dot(np.dot(np.linalg.inv(np.dot(ot,o)),ot),t)
  return w

"""----------y(x,w)方程式--------------"""
def summation(x,M,w):
  num=0
  for m in range(0,M+1):
    num=num+w[m]*pow(x,m)
  return num

"""0到7切100等分 用a不用x是因為x已被訂為train資料只有20個"""
"""----------畫圖--------------"""
def plot(M):
  a=np.linspace(0, 7, 100)
  y=summation(a,M,w1)
  plt.figure()
  plt.plot(x, t,'o')
  plt.plot(a, y,'-')
  plt.xlabel('x')
  plt.ylabel('t')
  plt.show()
for times in range(1,10):
  arr=x_arr(x,times)
  w1=matrix(t,arr)
  plot(times)

"""----------error_rms training data--------"""
w1=[]
error_rms=[]
for M in range(1,10):
   error=0
   arr=x_arr(x,M)
   w1=matrix(t,arr)
   for i in range(0,20): 
      error=error+(summation(x[i],M,w1)-t[i])**2
      if M==9:
        a=error
   error_rms.append(np.sqrt(error/20))
y1=error_rms

"""-----------error_rms test data------------"""
w2=[]
error_rms2=[]
for M in range(1,10):
   error2=0
   arr2=x_arr(x2,M)
   w2=matrix(t2,arr2)
   for i in range(0,10): 
      error2=error2+(summation(x2[i],M,w2)-t2[i])**2
   if M==9:
        b=error2
   error_rms2.append(np.sqrt(error2/10))
y2=error_rms2
"""-----------------------------------------------"""
xx=[]
for i in range(1,10):
    xx.append(i)
plt.figure()
plt.plot(xx, y1,'-o')
plt.plot(xx, y2,'-*')
plt.xlabel('M')
plt.ylabel('ERMS')
plt.show()

"""------------------------------------------"""

def ww(w):
    ww=np.dot(w.transpose(),w)
    return ww
def new_rms(error,l,w):
    r=error+exp(l)*0.5*ww(w)
    return r
l1=[]
l2=[]
"""------training--------""" 
def l1(i):
  ot=np.vstack(arr)
  o=np.vstack(arr).transpose() 
  w3=np.dot(np.dot(np.linalg.inv(np.dot(ot,o)+exp(i)*np.eye(10)),ot),np.vstack(t))
  l1=np.sqrt(new_rms(a,i,w3)/20)
  return l1

"""------testing---------"""
def l2(i):
  ot=np.vstack(arr2)
  o=np.vstack(arr2).transpose()
  w4=np.dot(np.dot(np.linalg.inv(np.dot(ot,o)+exp(i)*np.eye(10)),ot),np.vstack(t2))
  l2=np.sqrt(new_rms(b,i,w4)/10)
  return l2
"""----------------------"""
ll=np.linspace(-20,0, 100)
y3=[]
y4=[]

for i in range(0,100):
  y3.append(l1(ll[i]))
  y4.append(l2(ll[i]))
plt.figure()
plt.plot(ll, np.vstack(y3),'-')
plt.plot(ll, np.vstack(y4),'-')
plt.xlabel('lnλ')
plt.ylabel('ERMS')
plt.show()
















