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

