#!/usr/bin/env python
# -*- coding: utf-8 -*-min = 1
max = 100

print("Prime numbers between",min,"and"max,"are:")

for num in range(min,max + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
