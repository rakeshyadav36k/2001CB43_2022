def attendance_report():
    roll_numbers = [str(i) for i in registered_students['Roll No']]   # list of registered student

    date_list = list({datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").date() for i in df['Timestamp']  if datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").strftime('%a') in ['Mon','Thu']})
    #list of dates in which days are Monday and Thursday

    date_list.sort()

    duplicate = {date : {} for date in date_list}  # dictionary for storing the duplicate entries for each date

    duplct_info = {roll_number : {date.strftime('%d-%m-%Y') : 0 for date in date_list} for roll_number in roll_numbers}
    attended_dates = {roll_number : [] for roll_number in roll_numbers}
    fake_atten=[]
    fake_info = {roll_number : {date.strftime('%d-%m-%Y') : 0 for date in date_list} for roll_number in roll_numbers}
    

from platform import python_version    #  imported some libraries
from datetime import datetime
start_time = datetime.now()
ver = python_version()
import pandas as pd
import csv
# We read the input files into a pandas dataframe each
registered_students=pd.read_csv("input_registered_students.csv")   # read the csv file using panadas
df=pd.read_csv("input_attendance.csv")            # created a dataframe
df1=pd.DataFrame()
df1['Roll']=registered_students['Roll No'].copy()
df1['Name']=registered_students['Name'].copy()
actl_atten=[]
attendance_report()

df1.to_excel('./output/attendance_report_consolidated.xlsx',index=False)



end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))