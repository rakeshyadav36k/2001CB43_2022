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

    for i in range(len(df['Timestamp'])):      # loop is to find the students who have actual attendence, fake attendance & duplicate attendance
        ect = datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M')
        date = ect.date()
        
        if ect.weekday() == 0 or ect.weekday() == 3:  #Check if the person attended the class on monday or thursday
            if(ect.hour<14 or ect.hour>=15):
                fake_atten.append((str(df['Attendance'][i])).split(" ")[0])
                fake_info[(str(df['Attendance'][i])).split(" ")[0]][date.strftime('%d-%m-%Y')]+=1
            if(ect.hour==14):
                student_roll_no=(str(df['Attendance'][i])).split(" ")[0]
                if student_roll_no == 'nan' or student_roll_no not in roll_numbers:
                    continue
                if student_roll_no in duplicate[date]:
                    duplicate[date][student_roll_no]['entries'].append(ect)
                    duplct_info[(str(df['Attendance'][i])).split(" ")[0]][date.strftime('%d-%m-%Y')]+=1
                else:
                    duplicate[date][student_roll_no] = {'name': df['Attendance'][i].split(' ', 1)[1], 'entries': [ect]}
                    attended_dates[student_roll_no].append(date.strftime('%d-%m-%Y'))
                    actl_atten.append(student_roll_no)       
        else:
            fake_atten.append((str(df['Attendance'][i])).split(" ")[0])
        
    for i in range(len(registered_students['Name'])):   #loop is to print the attendance report for each student 
        
        for date in date_list:   # loop to check date on which date student are present or absent
            if date.strftime('%d-%m-%Y') in attended_dates[registered_students['Roll No'][i]]:
                dfc.at[i, date.strftime('%d-%m-%Y')]='P'
            else:
                dfc.at[i, date.strftime('%d-%m-%Y')]='A'
        dfc.at[i,'Actual Lecture Taken']=len(date_list)
        dfc.at[i,'Total Real Attendance']=actl_atten.count(registered_students['Roll No'][i])
        dfc.at[i,'Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal']=(round((dfc['Total Real Attendance'][i]/len(date_list))*100,2))
 
        seperate = pd.DataFrame()    # taken a dataframe to store the attendence of all students
        seperate.at[0, 'Date']=''
        for j,date in enumerate(date_list):
            seperate.at[j+1, 'Date'] = date.strftime('%d-%m-%Y')
        seperate.at[0,'Roll No'] = registered_students['Roll No'][i]
        seperate.at[0,'Name'] = registered_students['Name'][i]
        seperate.at[0,'total_attendance_count']=''
        seperate.at[0,'Real']=actl_atten.count(registered_students['Roll No'][i])
        seperate.at[0,'Absent']=len(date_list)-actl_atten.count(registered_students['Roll No'][i])
        for j,date in enumerate(date_list):
            seperate.at[j+1,'invalid']=fake_info[(str(df['Attendance'][i])).split(" ")[0]][date.strftime('%d-%m-%Y')]
            seperate.at[j+1, 'duplicate']=duplct_info[registered_students['Roll No'][i]][date.strftime('%d-%m-%Y')]
            if date.strftime('%d-%m-%Y') in attended_dates[registered_students['Roll No'][i]]:
                seperate.at[j+1, 'Real']=1
                seperate.at[j+1, 'Absent']=0
            else:
                seperate.at[j+1, 'Absent']=1
                seperate.at[j+1, 'Real']=0
            seperate.at[j+1, 'total_attendance_count']=seperate.at[j+1, 'Real']+seperate.at[j+1,'invalid']+seperate.at[j+1, 'duplicate']
        try:
            seperate.to_excel('output/' + registered_students['Roll No'][i] + '.xlsx',index=False)
        except PermissionError:
            print("You don't have the permission to read/write in this directory. Please grant permission or change the working directory")



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