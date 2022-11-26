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
# attendance_report()

df1.to_excel('./output/attendance_report_consolidated.xlsx',index=False)



end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))