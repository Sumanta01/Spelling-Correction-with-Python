# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 02:47:22 2023

@author: KIIT
"""

from textblob import TextBlob

print("Enter the text :")
words=input().split()
words=[str(i) for i in words]
correct_words=[]
for i in words:
    correct_words.append(TextBlob(i))
    
print("Wrong words : ",words)

print("Correct Words are : ")
for i in correct_words:
    print(i.correct(),end=" ")