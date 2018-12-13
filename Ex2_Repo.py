#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:34:08 2018

@author: zinebmezzour
"""

#%%

import requests

def get_repo(username):
    
    url = "https://api.github.com/users/{}/repos".format(username)
    
    repository = requests.get(url).json()
    
    for repo in repository:
        
        
        print("Repo Name:{} \n Language:{} \n Stars:{} \n Url:{} \n".format(
                repo["name"],
                repo["language"],
                str(repo["stargazers_count"]),
                repo["url"]))
