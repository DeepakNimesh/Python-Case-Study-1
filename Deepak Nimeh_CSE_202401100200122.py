# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hR9-kzySt3QrJBlDMH1g1xgIn6fdqklJ
"""

a=int(input("Enter first cost: "))
b=int(input("Enter second cost: "))
c=int(input("Enter third cost: "))
d=a+b+c
if (d<=50):
  print("Total: ",d)
else:
  print("Total with discount: ",0.9*d)

