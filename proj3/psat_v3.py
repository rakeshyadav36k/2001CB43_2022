#https://youtu.be/0srus9mXEhk
import streamlit as st
import os
import ntpath
import glob
import pandas as pd
import numpy as np
import datetime
from pathlib import Path 
from datetime import datetime 

start_time = datetime.now() 
print(start_time.strftime("%c"))

fileList = open('input_file_list.txt', 'r')
files = fileList.readlines()
for file in files:
    input_filename = file.strip()
    
    base = (Path(input_filename).stem.strip())
    output_csv = base+".csv"
    
    header_list = ['Time','SL' ,'counter' ,'U','V','W','W1','AMP-U' ,'AMP-V' ,'AMP-W' ,'AMP-W1' ,'SNR_U','SNR_V','SNR_W','SNR-W1' ,'Corr_U','Corr_V','Corr_W','Corr-W1']
    dataframe = pd.read_csv(input_filename,delimiter=" +")
    dataframe.to_csv(output_csv, encoding='utf-8', header=header_list, index=False)

index=0
# corr= 70
# SNR= 15 
# Lambda=1.5
# k=1.5
g=9.81
# N=input_data['U'].count()


with open(r"Results_v2.csv",mode='a') as file_:
    file_.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(start_time.strftime("%c"),"average_velocity_U","average_velocity_V","average_velocity_W","U_variance_Prime","V_variance_Prime","W_variance_Prime","U_stdev_Prime","V_stdev_Prime","W_stdev_Prime","Skewness_U_Prime","Skewness_V_Prime","Skewness_W_Prime","Kurtosis_U_Prime","Kurtosis_V_Prime","Kurtosis_W_Prime","Reynolds_stress_u\'v\'","Reynolds_stress_u\'w\'","Reynolds_stress_v\'w\'","Anisotropy","M30","M03","M12","M21","fku_2d","Fku_2d","fkw_2d","Fkw_2d","fku_3d","Fku_3d","fkw_3d","Fkw_3d","TKE_3d","Q1_K_Value","Q2_K_Value","Q3_K_Value","Q4_K_Value","e","ED","Octant_plus_1","Octant_minus_1","Octant_plus_2","Octant_minus_2","Octant_plus_3","Octant_minus_3","Octant_plus_4","Octant_minus_4","Total_Octant_sample","Probability_Octant_plus_1","Probability_Octant_minus_1","Probability_Octant_plus_2","Probability_Octant_minus_2","Probability_Octant_plus_3","Probability_Octant_minus_3","Probability_Octant_plus_4","Probability_Octant_minus_4","Min_Octant_Count","Min_Octant_Count_id","Max_Octant_Count","Max_Octant_Count_id","\n"))


constant_fk2d = st.number_input('constant_fk2d',0.75)
multiplying_factor_3d = st.number_input('multiplying_factor_3d',0.50)
Shear_velocity = st.number_input('Shear_velocity',2.6**3)



# print("-"*25)
# print('1. C','2. S','3. A','4. C & S','5. C & A','6. S & A','7. C & S & A','8. all combine',sep='\n')

choose = st.selectbox("Choose an option",['1. C','2. S','3. A','4. C & S','5. C & A','6. S & A','7. C & S & A','8. all combine'])

# tch = int(input('Chose Filtering Method From Above:'))
tch = st.number_input("Choose Filtering Method From Above:",1)
if tch == 1:
    # corr = int(input('Enter thresold value C:'))
    corr = st.number_input("Enter thresold value C:")

elif tch == 2:
    # SNR = int(input('Enter thresold value S:'))
    SNR = st.number_input("Enter thresold value S:")
elif tch == 3:
    # Lambda = float(input('Enter Lambda value for A:'))
    Lambda = st.number_input("Enter Lambda value for A:")
    # k = float(input('Enter k value for A:'))
    k = st.number_input("Enter k value for A:")
    # print(Lambda,k)
elif tch == 4:
    # corr = int(input('Enter thresold value C:'))
    # SNR = int(input('Enter thresold value S:'))
    corr = st.number_input("Enter thresold value C:")
    SNR = st.number_input("Enter thresold value S:")
elif tch == 5:
    # corr = int(input('Enter thresold value C:'))
    # Lambda = float(input('Enter Lambda value for A:'))
    # k = float(input('Enter k value for A:'))
    corr = st.number_input("Enter thresold value C:")
    Lambda = st.number_input("Enter Lambda value for A:")
    k = st.number_input("Enter k value for A:")
elif tch == 6:
    # SNR = int(input('Enter thresold value S:'))
    # Lambda = float(input('Enter Lambda value for A:'))
    # k = float(input('Enter k value for A:'))
    SNR = st.number_input("Enter thresold value S:")
    Lambda = st.number_input("Enter Lambda value for A:")
    k = st.number_input("Enter k value for A:")
elif tch == 7 or tch==8:
    # corr = int(input('Enter thresold value C:'))
    # SNR = int(input('Enter thresold value S:'))
    # Lambda = float(input('Enter Lambda value for A:'))
    # k = float(input('Enter k value for A:'))
    corr = st.number_input("Enter thresold value C:")
    SNR = st.number_input("Enter thresold value S:")
    Lambda = st.number_input("Enter Lambda value for A:")
    k = st.number_input("Enter k value for A:")
else:
    st.warning("Please enter correct choice...")
    # print('Please enter correct choice...')
# print("*"*25)


# print('1. previous point','2. 2*last-2nd_last','3. overall_mean',
#       '4. 12_point_strategy','5. mean of previous 2 point',
#       '6. all seqential','7. all parallel',sep='\n')

option = st.selectbox("Choose an option ",['1. previous point','2. 2*last-2nd_last','3. overall_mean','4. 12_point_strategy','5. mean of previous 2 point','6. all seqential','7. all parallel'])
# sch = int(input('Chose Replacement Method From Above:')) 
sch = st.number_input("Chose Replacement Method From Above:")
if st.button("Compute"):
    if sch > 7 :
        # print('Please enter correct choice...')
        st.warning("Please enter correct choice...")
    else:
        fileList = open('input_file_list.txt', 'r')
        files = fileList.readlines()
        for file in files:
            input_filename=file.strip()[:-3]+'csv'
            try:
                input_data = pd.read_csv(input_filename)
            except:
                # print(input_filename)
                continue
            N=input_data['U'].count()

            if tch==1 or tch==8:
                if sch > 5:
                    iList = [1,2,3,4,5]
                else:
                    iList = [sch]
                for i in iList:
                    if sch==7:
                        input_data = pd.read_csv(input_filename)
                    data =input_data
                    find_mean()
                    find_std()
                    Corr_All(i,corr)
                    allfunction()
                    name = f"{input_filename}_filtered_by_correlation{corr}_all_replacement_strategy_{i}"
                    write_timestamp_to_file(name)
                    name = add_front_name(name,i)
                    store()

                    data =input_data
                    find_mean()
                    find_std()
                    Corr_One(i,corr)
                    allfunction()
                    name = f"{input_filename}_filtered_by_correlation{corr}_individual_replacement_strategy_{i}"
                    write_timestamp_to_file(name)
                    name = add_front_name(name,i)
                    store()

            if tch==2 or tch==8:
                if sch>5:
                    iList = [1,2,3,4,5]
                else:
                    iList = [sch]
                for i in iList:
                    if sch==7:
                        input_data = pd.read_csv(input_filename)
                    data =input_data
                    find_mean()
                    find_std()
                    SNR_All(i,SNR)
                    allfunction()
                    name = f"{input_filename}_filtered_by_SNR{SNR}_all_replacement_strategy_{i}"
                    write_timestamp_to_file(name)    
                    name = add_front_name(name,i)
                    store()

                    data =input_data
                    find_mean()
                    find_std()
                    SNR_One(i,SNR)
                    allfunction()
                    name = f"{input_filename}_filtered_by_SNR{SNR}_individual_replacement_strategy_{i}"
                    write_timestamp_to_file(name)
                    name = add_front_name(name,i)
                    store()

            if tch==3 or tch==8:
                if sch>5:
                    iList = [1,2,3,4,5]
                else:
                    iList = [sch]
                for i in iList:
                    if sch==7:
                        input_data = pd.read_csv(input_filename)
                    data =input_data
                    find_mean()
                    find_std()
                    update_acceleration_all_at_time(i)
                    allfunction()
                    name = f"{input_filename}_filtered_by_acceleration_1.5_all_replacement_strategy_{i}"
                    write_timestamp_to_file(name)
                    name = add_front_name(name,i)
                    store()

                    data =input_data
                    find_mean()
                    find_std()
                    update_acceleration_one_at_time(i)
                    allfunction()
                    name = f"{input_filename}_filtered_by_acceleration_1.5_individual_replacement_strategy_{i}"
                    write_timestamp_to_file(name)
                    name = add_front_name(name,i)
                    store()

            if tch==4 or tch==8:
                if sch>5:
                    iList = [1,2,3,4,5]
                else:
                    iList = [sch]
                for i in iList:
                    if sch==7:
                        input_data = pd.read_csv(input_filename)
                    data =input_data
                    find_mean()
                    find_std()
                    Corr_All(i,corr)
                    SNR_All(i,SNR)
                    allfunction()
                    name = f"{input_filename}_filtered_by_correlation{corr}_SNR{SNR}_all_replacement_strategy_{i}"
                    write_timestamp_to_file(name)
                    name = add_front_name(name,i)
                    store()

                    data =input_data
                    find_mean()
                    find_std()
                    Corr_One(i,corr)
                    SNR_One(i,SNR)
                    allfunction()
                    name = f"{input_filename}_filtered_by_correlation{corr}_SNR{SNR}_individual_replacement_strategy_{i}"
                    write_timestamp_to_file(name)
                    name = add_front_name(name,i)
                    store()

            if tch==5 or tch==8:
                if sch>5:
                    iList = [1,2,3,4,5]
                else:
                    iList = [sch]
                for i in iList:
                    if sch==7:
                        input_data = pd.read_csv(input_filename)
                    data =input_data
                    find_mean()
                    find_std()
                    SNR_All(i,SNR)
                    update_acceleration_all_at_time(i)
                    allfunction()
                    name = f"{input_filename}_filtered_by_SNR{SNR}_Acceleration_1.5_all_replacement_strategy_{i}"
                    write_timestamp_to_file(name)
                    name = add_front_name(name,i)
                    store()

                    data =input_data
                    find_mean()
                    find_std()
                    SNR_One(i,SNR)
                    update_acceleration_all_at_time(i)
                    allfunction()
                    name = f"{input_filename}_filtered_by_SNR{SNR}_acceleration_1.5_individual_replacement_strategy_{i}"
                    write_timestamp_to_file(name)
                    name = add_front_name(name,i)
                    store()

            if tch==6 or tch==8:
                if sch>5:
                    iList = [1,2,3,4,5]
                else:
                    iList = [sch]
                for i in iList:
                    if sch==7:
                        input_data = pd.read_csv(input_filename)
                    data =input_data
                    find_mean()
                    find_std()
                    Corr_All(i,corr)
                    update_acceleration_all_at_time(i)
                    allfunction()
                    name = f"{input_filename}_filtered_by_correlation{corr}_Acceleration_1.5_all_replacement_strategy_{i}"
                    write_timestamp_to_file(name)
                    name = add_front_name(name,i)
                    store()

                    data =input_data
                    find_mean()
                    find_std()
                    Corr_One(i,corr)
                    update_acceleration_all_at_time(i)
                    allfunction()
                    name = f"{input_filename}_filtered_by_correlation{corr}_acceleration_1.5_individual_replacement_strategy_{i}"
                    write_timestamp_to_file(name)
                    name = add_front_name(name,i)
                    store()

            if tch==7 or tch==8:
                if sch>5:
                    iList = [1,2,3,4,5]
                else:
                    iList = [sch]
                for i in iList:
                    if sch==7:
                        input_data = pd.read_csv(input_filename)
                    data =input_data
                    find_mean()
                    find_std()
                    Corr_All(i,corr)
                    SNR_All(i,SNR)
                    update_acceleration_all_at_time(i)
                    allfunction()
                    name = f"{input_filename}_filtered_by_correlation{corr}_SNR{SNR}_Acceleration_1.5_all_replacement_strategy_{i}"
                    write_timestamp_to_file(name)

                    name = add_front_name(name,i)
                    store()

                    data =input_data
                    find_mean()
                    find_std()
                    Corr_One(i,corr)
                    SNR_One(i,SNR)
                    update_acceleration_all_at_time(i)
                    allfunction()
                    name = f"{input_filename}_filtered_by_correlation{corr}_SNR{SNR}_acceleration_1.5_individual_replacement_strategy_{i}"
                    write_timestamp_to_file(name)    
                    name = add_front_name(name,i)
                    store()