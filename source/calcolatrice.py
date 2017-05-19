'''
Created on 10 mag 2017

@author: Enrico
'''
import math
from math import sqrt, sin, cos

class calcolatrice(object):
    
    def somma(self, num1, num2):
        return num1+num2
    
    def differenza(self, num1, num2):
        return num1-num2
    
    def moltiplica(self, num1,num2):
        return num1*num2
    
    def dividi(self, num1, num2):
        return num1/num2
    
    def modulo(self, num1, num2):
        return num1%num2
    
    def potenza(self, num, potenza):
        return num ** potenza
    
    def radiceQuadrata(self, num):
        return sqrt(num)
    
    def seno(self, num):
        return sin(num)
    
    def coseno(self, num):
        return cos(num)
    
    def logaritmoBase2(self, num):
        return math.log2(num)
    
    def intToBit(self, num):
        return int(bin(num+2**32)[-32:])
