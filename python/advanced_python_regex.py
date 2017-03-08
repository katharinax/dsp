#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 21:35:35 2017

@author: katharina
"""

import numpy as np
import pandas as pd
import re

df = pd.read_csv("faculty.csv", sep = r",\s*", engine="python")

# Q1
degree_ct = {}
for dgstring in df["degree"]:
    for dg in re.finditer(r"(?:^|\s)[\w\.]+(?=$|\s)", dgstring):
        dg_cleaned = re.sub("[\. ]", "", dg.group(0))
        if re.match(r"(?i)[a-z]+", dg_cleaned) != None:
            if dg_cleaned not in degree_ct.keys():
                degree_ct[dg_cleaned] = 1
            else:
                degree_ct[dg_cleaned] += 1
degree_ct = pd.DataFrame(list(degree_ct.items()), columns = ["Degree", "N"])
degree_ct = degree_ct.sort_values("N", ascending = False)
print("There are a total of", degree_ct.shape[0], "different degrees.\n")
print(degree_ct.to_string(index = False)) 

# Q2
title_ct = {}
for t in df["title"]:
    t_cleaned = re.sub(r" ((of)|(is)) Biostatistics", "", t)
    if t_cleaned not in title_ct.keys():
        title_ct[t_cleaned] = 1
    else:
        title_ct[t_cleaned] += 1
title_ct = pd.DataFrame(list(title_ct.items()), columns = ["Title", "N"])
title_ct = title_ct.sort_values("N", ascending = False)
print("There are a total of", title_ct.shape[0], "different titles.\n")
print(title_ct.to_string(index = False)) 
   