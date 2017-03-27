# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 09:52:21 2017

@author: Umair.Hanif
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

my_data= pd.read_csv("C://Users//umair.hanif//Desktop//Learning Outcomes//UmairHanif_KHI_Python_Assignment2//hospitaldata.csv")

#Q1
for i in my_data.columns:
    if ".." in i:
        my_data.rename(columns={i: i.replace('..','_')}, inplace=True)
        
print(my_data.head())

#Q2
date=my_data['Date']
days=date.map(lambda x: str(x).split(',')[0])
counts=days.value_counts()
print(counts)

#Q3
my_data['Age']=pd.to_numeric(my_data['Age'],errors='coerce' )
my_data['Age'].mean()


#Q4
children=my_data[my_data.Age<=12]
len(children.index)

#Q5
str=my_data.Sex
str.replace("f", "F")
Male=my_data[my_data.Sex=='M']
Female=my_data[my_data.Sex=='F']
print("Male:" ,Male['Procedure'].value_counts().index.tolist()[0])
print("Female:" ,Female['Procedure'].value_counts().index.tolist()[0])


#Q6
my_data['Total_Charges']=pd.to_numeric(my_data['Total_Charges'],errors='coerce')
highest_earn = my_data[['Consulting_Doctor', 'Total_Charges']].groupby(['Consulting_Doctor']).sum()
print(highest_earn) # showing DR.Alaf khan is earning highest income


#Q7
proc=my_data[['Procedure', 'Total_Charges']].groupby(['Procedure']).sum()
print(proc)


#Q8
my_data.Time=pd.to_datetime(my_data.Time, errors='coerce')
my_data.Time.dt.hour.value_counts() # shows at 13th hours means 1 AM/PM the most patients had arrived

                
#Q9
def time_bracket(hour):
    if  hour>= 6.0 and hour<12.0:
        return "Morning"
    elif hour>= 12 and hour<14:
        return "Afternoon"
    elif  hour>=14 and hour<19 :
        return "Evening"
    elif  hour>=19 and hour<=23 or hour >= 0 and hour < 6 :
        return "Night"
    
my_data['Time_brackets']=my_data.Time.dt.hour.apply(time_bracket)


#Q10
rep_patients=my_data['id'].value_counts()
print(len(rep_patients[rep_patients>1].index))


#Q11
print("Id \t Visits\n",rep_patients)


#Q12
x=my_data[['id','Procedure']]
patient_visits=x.groupby(['id','Procedure']).size()
print(patient_visits[patient_visits>1])


#Q13
f_median=Female.Age.median()
m_median=Male.Age.median()
print("Female Age Median: ", f_median)
print("Male Age Median: ", m_median)


#Q15
consult_charges=my_data[my_data.Procedure=='Consultation']
consult_charges['Total_Charges'].sum()


#Q16
Cor=my_data.corr()
Cor.loc[['Age'],['Total_Charges']]


#Q17
my_data['Age'].plot.hist()
plt.show()


#Q18
my_data[(my_data.Procedure== 'X Rays') | (my_data.Procedure == 'Scalling')]['Total_Charges'].sum()

