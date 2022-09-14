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

U_avg = U_total/count            # here we have calculated the average of U, V & W
V_avg = V_total/count
W_avg = W_total/count

length1 = length2 = length3 = 0               
list_1 = []                          # we declare three empty list in which we can store the value of U', V' & W'
list_2 = []
list_3 = []

with open("octant_input.csv","r") as ft:         # we have again opened the octant_input.csv file in read mode
    info = csv.reader(ft)
    for x in info:
        if(x[1]!='U'):
            list_1.insert(length1,float(x[1])-U_avg)     # here we have inserted the value of U'= U - U_avg, V'= V - V_avg & W'= W - W_avg in the list
            length1+=1
        if(x[2]!='V'):
            list_2.insert(length2,float(x[2])-V_avg)
            length2+=1
        if(x[3]!='W'):
            list_3.insert(length3,float(x[3])-W_avg)
            length3+=1

# print(list_1)
# print(list_2)
# print(list_3)


i = 0      # i is the index
count_positive_1 = count_positive_2 = count_positive_3 = count_positive_4 = 0    # initialization of octant value that tells howmany times the octant present 
count_negative_1 = count_negative_2 = count_negative_3 = count_negative_4 = 0           