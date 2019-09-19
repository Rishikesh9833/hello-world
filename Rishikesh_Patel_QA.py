# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:27:38 2019

@author: admin
"""
def get_cksum(s):
    i = 0;
    sum = 0;
    while i < len(s):
        num = int(s[i:i+2],16)
        #print(num)
        i=i+2
        sum = sum+num    
        
    #print(sum)
    cksum=sum % 255
    print(cksum)
   
get_cksum('ABCDEF1234567890')