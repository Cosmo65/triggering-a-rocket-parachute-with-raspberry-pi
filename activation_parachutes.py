# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:48:19 2019

@author: Samsung
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import serial
import time
porta = 'COM9'
velocidade = 9600
vet=[]
vet_acionamento=[]
conexao = serial.Serial(porta,velocidade)
for i in range(0,15):
    leitura_serial = conexao.readline()
    leitura_limpa=leitura_serial.split()
    leitura_limpa1=str(leitura_limpa).strip('[]')
    leitura_limpa2=leitura_limpa1.replace('b','')
    leitura_limpa3=str(leitura_limpa2).strip("''")
    print(leitura_limpa3.split())
    vet.append(leitura_limpa3)
    for i in range (len(vet)):
        if vet[i]>vet[i-1] and vet[i]<vet[i-2] and i!=0 and i!=1:
            print(vet[i])
            conexao.write(b'H')   
print(vet)
def hl(numbers):
    y = []
    for x in numbers:
        x = float(x)
        y.append(x)
    return y
print(hl(vet))
x=hl(vet)
y=[]
for i in range(0,len(x)):
    y.append(i)
d={'distancia':hl(vet)}
df=pd.DataFrame(data=d)
print(df)
plt.plot(y, x)
plt.title('Distancia x tempo')
plt.show()

    

