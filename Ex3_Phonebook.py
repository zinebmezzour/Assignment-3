#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:17:15 2018

@author: zinebmezzour
"""
#%%

from flask import Flask, jsonify


phonebook = {
        "Zineb": "666777888",
        "Pepe": "098308308" }


server = Flask("PhoneBook server")



# Get a phone by name    
@server.route("/contact/<name>")
def get_contact_phone(name):
    
    if name in phonebook :
        contact = phonebook[name]
        return jsonify(contact)
    else:
        return jsonify("Contact not existant")
    

#Add contact
@server.route("/add/<name>/<phone>", methods=["POST"])    
def add_contact(name,phone):
    phonebook[name] = phone
    return jsonify({"Message":"Contact Added","Contact name":name,"Contact number":phone})


#Delete a contact
@server.route("/delete/<name>", methods=["POST"])
def delete_number(name):
    phonebook.pop(name)
    return jsonify({"Message":"Contact deleted","Contact name":name})

#update a phone by name

@server.route("/update/<name>/<number>", methods=["POST"])
def update_number(name,number):
    phonebook[name] = number 
    return jsonify({"Message":"Contact number updated","Contact name":name,"Contact number":number})



server.run()            
