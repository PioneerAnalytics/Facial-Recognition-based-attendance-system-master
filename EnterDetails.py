# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:36:44 2019

@author: MAYANK
"""

import os
from datetime import datetime;
import mysql.connector;
#creating instance of TK
root=Tk()
pas=input("enter admin Password")
mydb = mysql.connector.connect(host="localhost",user="root",passwd=pas,database="student_database")
mycursor = mydb.cursor()

name=input("enter name")
rid=int(input("enter rolll no."))
clss=input("enter class")
stats="Absent"
from datetime import date
today = date.today()
# dd/mm/YY
d = today.strftime("%d/%m/%Y")

sql="INSERT INTO Attendance values(name,roll_no,class,stats,datte );"\ "VALUES(%s,%d,%s,%s,%s)"

args = (name, rid,clss,stats,d);
mycursor.executemany(sql,args);
mydb.commit();
print(mycursor.rowcount, "record inserted.")
s = "update Attendance SET datte=current_date();"
mycursor.execute(s);
mydb.commit()
print(mycursor.rowcount, "record inserted.")
print("Database updated")

