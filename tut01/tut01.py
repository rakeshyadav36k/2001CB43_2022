# def octact_identification(mod=5000):
# ###Code


#     from platform import python_versions
#     ver = python_version()

#     if ver == "3.8.10":
#         print("Correct Version Installed")
#     else:
#         print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

# mod=5000
# octact_identification(mod)


import os
import csv

os.system("cls")

with open("octant_input.csv","r") as ft:  # first we read the octant_input.csv file
    info = csv.reader(ft)

    U_total = V_total = W_total = 0        # we initialize the total value of U, V & W with 0
    count = 0                         # initialize the total no of rows with 0
    
    for line in info:
        if(line[1]!='U'):
            U_total+=float(line[1]) 
        if(line[2]!='V'):
            V_total+=float(line[2])
        if(line[3]!='W'):
            W_total+=float(line[3])
        count+=1

