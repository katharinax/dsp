#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:19:56 2017

@author: katharina
"""

def print_first3(dic):
    counter = 1
    for key in dic.keys():
        if counter <= 3:
            print(str(key)+":", dic[key])
        counter += 1
    
runfile("advanced_python_regex.py")
name_df = pd.DataFrame([re.split(r"\s+", name) for name in df["name"].tolist()])
df["lname"] = np.where(name_df[2].isnull(), name_df[1], name_df[2])
df["fname"] = np.where(name_df[2].isnull(), name_df[0], 
  np.where(name_df[0].str.contains(r"\."), name_df[1], name_df[0]))

# Q6
faculty_dict = {}
for index, row in df.iterrows():
    lname = row["lname"]
    value = list(row[["degree", "title", "email"]])
    value[1] = re.sub(r" ((of)|(is)) Biostatistics", "", value[1])
    if lname in faculty_dict.keys():
        faculty_dict[lname] += [value]
    else:
        faculty_dict[lname] = [value]
print_first3(faculty_dict)

# Q7
professor_dict = {}
for index, row in df.iterrows():
    key = tuple(row[["fname", "lname"]])
    value = list(row[["degree", "title", "email"]])
    value[1] = re.sub(r" ((of)|(is)) Biostatistics", "", value[1])
    if key in professor_dict.keys():
        raise ValueError("There are people with the same name")
    professor_dict[key] = value
print_first3(professor_dict)

# Q8
professor_dict_sorted = dict(sorted(professor_dict.items(), 
  key = lambda i: i[0][0]))
for key in professor_dict_sorted.keys():
    print(str(key)+":", professor_dict_sorted[key])






