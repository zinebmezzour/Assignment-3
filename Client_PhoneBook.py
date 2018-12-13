#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 20:00:46 2018

@author: zinebmezzour
"""

#%%

# Phone Book 

# CLIENT 

import requests


localhost = "http://127.0.0.1:5000"

def get_contact(name):
   response = requests.get(localhost+"/contact/"+name)
   if response.status_code == 200:
       return response.json()
   else:
       return print(response.status_code)


def add_contact(name,phone):
    response = requests.post(localhost+"/add/"+name+"/"+phone)
    if response.status_code == 200:
        return response.json()
    else:
       return print(response.status_code)

def delete_contact(name):
    response = requests.post(localhost+"/delete/"+name)
    if response.status_code == 200:
        return response.json()
    else:
       return print(response.status_code)

def update_contact(name,number):
    response = requests.post(localhost+"/update/"+name+"/"+number)
    if response.status_code == 200:
        return response.json()
    else:
       return print(response.status_code)
   

