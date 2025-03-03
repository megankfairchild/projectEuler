#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:06:35 2024

@author: meganfairchild
pyhagorean problem

a2 + b2 = c2
a+b+c=1000
c=1000-b-a
a2 + b2 = (1000 - b - a)2
"""

def pythag(num1, num2):
    num1=num1
    num2=num2
    #function that determines whether or not the given tuple is a pythagorean triple
    c = 1000-num1-num2
    if (num1*num1)+(num2*num2)==(c*c):
        return True 
    else:
        return False 
    
a=1
while a<1000:
    b=1
    while b<1000:
        boolfool = pythag(a, b)
        if boolfool:
            c=1000-a-b
            print("a is: ", a, "b is: ", b, "c is: ", c)
            print("the product abc is: ", a*b*c)
            a=1000
            b=1000
        else:
            b+=1
    a+=1 
        
"""
Congratulations, the answer you gave to problem 9 is correct.

You are the 379165th person to have solved this problem.

This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%.
"""     