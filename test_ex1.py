#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:15:11 2018

@author: zinebmezzour
"""

#%%

from exercice1 import Product
from exercice1 import recalculate_quality


potato = Product("potato",10)
cheese = Product("cheese",6)
salad = Product("salad",4)
chips = Product("chips",5)
orange = Product("orange",1)

#potato2= potato.quality - 0.5
#cheese2 = cheese.quality - 2
#salad2 = salad.quality - 3
#chips2 = chips.quality 
#orange2= orange.quality - 3

potato2 = Product("potato",9.5)
cheese2 = Product("cheese",4)
salad2 = Product("salad",1)
chips2 = Product("chips",5)
orange2 = Product("orange",-2)

def test_quality_product_before():
    assert potato.quality == 10
    assert cheese.quality == 6
    assert salad.quality == 4
    assert chips.quality == 5
    assert orange.quality == 1
    

def test_quality_product_after():
    recalculate_quality(potato)
    assert potato.quality == 9.5
    recalculate_quality(cheese)
    assert cheese.quality == 4
    recalculate_quality(salad)
    assert salad.quality == 1
    recalculate_quality(chips)
    assert chips.quality == 5
    recalculate_quality(orange)
    assert orange.quality == -2


def test_quality_product_before_second_round():
    assert potato2.quality == 9.5
    assert cheese2.quality == 4
    assert salad2.quality == 1
    assert chips2.quality == 5
    assert orange2.quality == -2

def test_quality_product_after_second_round():
    recalculate_quality(potato2)
    assert potato2.quality == 9
    recalculate_quality(cheese2)
    assert cheese2.quality == 2
    recalculate_quality(salad2)
    assert salad2.quality == -2
    recalculate_quality(chips2)
    assert chips2.quality == 5
    recalculate_quality(orange2)
    assert orange2.quality == -5


