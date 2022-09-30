# def octant_transition_count(mod=5000):
# ###Code

# from platform import python_version
# ver = python_version()

# if ver == "3.8.10":
#     print("Correct Version Installed")
# else:
#     print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

# mod=5000
# octant_transition_count(mod)




# I have imported some libraries
from openpyxl import load_workbook
import numpy as np
import pandas as pd

wb = load_workbook('input_octant_transition_identify.xlsx')     # I have opened the Excel file
sheet = wb.active

df = pd.read_excel('input_octant_transition_identify.xlsx')     # df is a data frame in which we put the data of excel file using pandas

sheet.cell(row=1, column=5).value = "U Avg"       # Written the header 
sheet.cell(row=1, column=6).value = "V Avg" 
sheet.cell(row=1, column=7).value = "W Avg"  
sheet.cell(row=1, column=8).value = "U'=U - U avg" 
sheet.cell(row=1, column=9).value = "V'=V - V avg" 
sheet.cell(row=1, column=10).value = "W'=W - W avg"

Uavg = df['U'].mean()     # calculated the mean using pandas
Vavg = df['V'].mean()
Wavg = df['W'].mean()

sheet.cell(row=2, column=5).value = Uavg   # added the average values in the sheet
sheet.cell(row=2, column=6).value = Vavg 
sheet.cell(row=2, column=7).value = Wavg 

l1 = df['U']            # creating the list l1,l2,l3 which consist the element of U,V,W respectively
l2 = df['V']
l3 = df['W']


# creating three lists l4,l5 & l6 which contains the values of U', V' & W'

#********************   
l4=[]
for i in l1:
    a = i - Uavg
    l4.append(a)

for i in range(2,len(l1)+2):
    sheet.cell(row=i, column=8).value = l4[i-2]

l5=[]
for i in l2:
    a = i - Vavg
    l5.append(a)

for i in range(2,len(l2)+2):
    sheet.cell(row=i, column=9).value = l5[i-2]

l6=[]
for i in l3:
    a = i - Wavg
    l6.append(a)

for i in range(2,len(l3)+2):
    sheet.cell(row=i, column=10).value = l6[i-2]

#************************************

# here we have created a header "Octant" and print the values of octants in excel file

sheet.cell(row=1, column=11).value = "Octant"



for i in range(0,len(l1)):
    if(l4[i]>0 and l5[i]>0):
        if(l6[i]>0):
            sheet.cell(row=i+2, column=11).value = "+1"
        else:                                               # this tells whether the octant is +1 or -1
            sheet.cell(row=i+2, column=11).value = "-1"
    elif(l4[i]<0 and l5[i]>0):
        if(l6[i]>0):
            sheet.cell(row=i+2, column=11).value = "+2"
        else:                                               # this tells whether the octant is +2 or -2
            sheet.cell(row=i+2, column=11).value = "-2"
    elif(l4[i]<0 and l5[i]<0):
        if(l6[i]>0):
            sheet.cell(row=i+2, column=11).value = "+3"
        else:                                                # this tells whether the octant is +3 or -3
            sheet.cell(row=i+2, column=11).value = "-3"
    elif(l4[i]>0 and l5[i]<0):
        if(l6[i]>0):
            sheet.cell(row=i+2, column=11).value = "+4"
        else:                                                 # this tells whether the octant is +4 or -4
            sheet.cell(row=i+2, column=11).value = "-4"
    
        
#888888888888
# l7 = df['Octant']  # this list l7 contains the all octants values
l7=[]
for i in range(len(l1)):
    x=sheet.cell(row=i+2,column=11).value
    l7.append(int(x))


sheet['M2']="Overall Count"  # this is basicallly printed the header
sheet['N1'] = "+1"
sheet['O1'] = "-1"
sheet['P1'] = "+2"
sheet['Q1'] = "-2"
sheet['R1'] = "+3"
sheet['S1'] = "-3"
sheet['T1'] = "+4"
sheet['U1'] = "-4"

ctpos1 = ctneg1 = ctpos2 = ctneg2 = ctpos3 = ctneg3 = ctpos4 = ctneg4 = 0  # these variables are total no each octant present

for i in range(0,len(l1)):
    if(l4[i]>0 and l5[i]>0):
        if(l6[i]>0):
            ctpos1 += 1               # total count of octant no +1 & -1
        else:
            ctneg1 += 1
    elif(l4[i]<0 and l5[i]>0):
        if(l6[i]>0):
            ctpos2 += 1                 # total count of octant no +2 & -2
        else:
            ctneg2 += 1
    elif(l4[i]<0 and l5[i]<0):
        if(l6[i]>0):
            ctpos3 += 1                 # total count of octant no +3 & -3
        else:
            ctneg3 += 1
    elif(l4[i]>0 and l5[i]<0):
        if(l6[i]>0):
            ctpos4 += 1                 # total count of octant no +4 & -4
        else:
            ctneg4 += 1


#  we have inserted the values of total no of each count

sheet.cell(row=2, column=14).value = ctpos1
sheet.cell(row=2, column=15).value = ctneg1
sheet.cell(row=2, column=16).value = ctpos2
sheet.cell(row=2, column=17).value = ctneg2
sheet.cell(row=2, column=18).value = ctpos3
sheet.cell(row=2, column=19).value = ctneg3
sheet.cell(row=2, column=20).value = ctpos4
sheet.cell(row=2, column=21).value = ctneg4
