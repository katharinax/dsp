#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:44:13 2017

@author: katharina
"""

runfile("advanced_python_regex.py")

file = open("emails.csv", "w+")
for email in email_list:
    file.write(email)
    file.write("\n")
file.close() 

