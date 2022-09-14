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

while(i<len(list_1)):
    if(list_1[i]>0 and list_2[i]>0):           # these are the codes to calculate the each octant
        if(list_3[i]>0):                       # this is for whether the octant is -1 or 1
            count_positive_1+=1
        else:
            count_negative_1+=1
    elif(list_1[i]<0 and list_2[i]>0):          # this is for whether the octant is -2 or 2
        if(list_3[i]>0):
            count_positive_2+=1
        else:
            count_negative_2+=1
    elif(list_1[i]<0 and list_2[i]<0):         # this is for whether the octant is -3 or 3
        if(list_3[i]>0):
            count_positive_3+=1
        else:
            count_negative_3+=1
    elif(list_1[i]>0 and list_2[i]<0):        # this is for whether the octant is -4 or 4
        if(list_3[i]>0):
            count_positive_4+=1
        else:
            count_negative_4+=1

    i+=1

print("number of octants : ")          # we printed the no of octants
print("total no of '1' octant : ",count_positive_1)
print("total no of '-1' octant : ",count_negative_1)
print("total no of '2' octant : ",count_positive_2)
print("total no of '-2' octant : ",count_negative_2)
print("total no of '3' octant : ",count_positive_3)
print("total no of '-3' octant : ",count_negative_3)
print("total no of '4' octant : ",count_positive_4)
print("total no of '-4' octant : ",count_negative_4)

###  now we writing the codes howmany times octants are present in a particular range

def octant_finding(mod):
    j=k=0
    num = mod
    
    while(j<len(list_1)/num):
        mod_ct_pos1=mod_ct_pos2=mod_ct_pos3=mod_ct_pos4=mod_ct_neg1=mod_ct_neg2=mod_ct_neg3=mod_ct_neg4 = 0
    
        while(k<mod):
            if(list_1[k]>0 and list_2[k]>0):           # this is for whether the octant is -1 or 1
                if(list_3[k]>0):
                    mod_ct_pos1+=1
                else:
                    mod_ct_neg1+=1

            elif(list_1[k]<0 and list_2[k]>0):         # this is for whether the octant is -2 or 2
                if(list_3[k]>0):
                    mod_ct_pos2+=1
                else:
                    mod_ct_neg2+=1

            elif(list_1[k]<0 and list_2[k]<0):           # this is for whether the octant is -3 or 3
                if(list_3[k]>0):
                    mod_ct_pos3+=1
                else:
                    mod_ct_neg3+=1

            elif(list_1[k]>0 and list_2[k]<0):           # this is for whether the octant is -4 or 4
                if(list_3[k]>0):
                    mod_ct_pos4+=1
                else:
                    mod_ct_neg4+=1

            k+=1
        mod+=num
        j+=1
        
        print("the count value for given mod :  ")
        print(mod_ct_pos1)       
        print(mod_ct_pos2)       
        print(mod_ct_pos3)       
        print(mod_ct_pos4) 
        print(mod_ct_neg1)      
        print(mod_ct_neg2)      
        print(mod_ct_neg3)      
        print(mod_ct_neg4)   

mod = int(input("enter the value of mod : "))   
octant_finding(mod)
            