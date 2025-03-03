#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:35:18 2024

@author: meganfairchild

difference between (sum of squares) and (square of sum)
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(num):
    num=num+1
    print("num in sum of squares is: ", num)
    i=1
    sumnums=0
    while(i<num):
        j=i*i
        print("i is ", i, "and j is ", j)
        sumnums=sumnums+j
        print("sumnums is ", sumnums)
        i+=1
    return(sumnums)

def square_of_sums(num):
    num=num+1
    sumnums=0
    i=1
    while i<num:
        sumnums=sumnums+i
        i+=1
    product = sumnums*sumnums 
    return(product)

num=100
sum_square = sum_of_squares(num)
square_sum = square_of_sums(num)
print("sum of squares is ", sum_square, "square of sum is ", square_sum)
diff = square_sum - sum_square

print("the answer is ", diff)    

"""
Congratulations, the answer you gave to problem 6 is correct.

You are the 521601st person to have solved this problem.

This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%
"""    