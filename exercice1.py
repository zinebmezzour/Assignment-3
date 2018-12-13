#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 16:28:37 2018

@author: zinebmezzour
"""

#%%

class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
   

potato = Product("potato",10)
cheese = Product("cheese",6)
salad = Product("salad",4)
chips = Product("chips",5)
orange = Product("orange",1)

def recalculate_quality(product):
    if product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
          
       
    else:
        if product.quality < 5:
            product.quality -= 3
        
       