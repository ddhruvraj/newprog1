# class student:
#
#     def showdata(self):
#         return f" name is {self.roll_no} and salary is {self.name} \n role is {self.course}"
#
#     def __int__(self, aroll_no, aname, acourse):
#         self.roll_no = aroll_no
#         self.name = aname
#         self.course = acourse
#
# abc=student(1,"sda","erve")
#
# print(abc.showdata())


#
# class employee:
#     leave_of_employee=8
#     pass
#
#     def printdetails(self):
#         print("roll no:",self.name,self.salary,self.role)
#
#     def __init__(self,aname,asalary,arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#
#
#
# dhruv=employee("dhruv",1234,"faculty")
# print(dhruv.printdetails())


# class abc:
#     pass
# dhruv=abc()
# dhruv.name=35
# print(dhruv.name)

# class pqr:
#
#     def printdetails(self):
#         return f"name is {self.name},roll number is {self.roll_no},course is {self.course}"
#
# dhruv=pqr()
#
# dhruv.name="dhruv"
# dhruv.roll_no=23
# dhruv.course="raj"
#
# print(dhruv.printdetails())


# password generator

#
# import random
#
# lower="qwertyuiopasdfghjklzxcvbnm"
# upper="ASDFGHJKLQWERTYUIOPZXCVBNM"
# num="0987654321"
# symbol="*&@!#$"
# all=lower+upper+num+symbol
# # length=9
# # password="".join(random.sample(all,length))
# # print(password)
# for i in range (9):
#     print(random.choice(all),end="")

# def x(values):
#     values[0]=1
# v=[2,3,4]
# x(v)
# print(v)

# import os
# # print(os.getcwd())
# # f=open("mylogs.txt")
# # print(os.listdir(""))
# def soldier(path,file,format):
#     os.chdir(path)
#     i = 1
#     files=os.listdir(path)
#     print(files)
#     with open(file) as f:
#         filelist=f.read().split("\n")
#
#     for file in filelist:
#         if file not in filelist:
#             os.rename(file,file.capitalize())
#
#         if os.path.splitext(file)[1]==format:
#             os.rename(file,f"{i}{format}")
#             i+=1
#
# soldier(r"C:\Users\vaghe\OneDrive\Desktop\testing",
#         r"C:\Users\vaghe\PycharmProjects\newprog\ex8.txt",".png")

# import requests

# x = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
#
# print(x.text)
# print(x.status_code)
# url="http://www.facebook.com"
# data={
#     "username":9723515696,
#     "password":"dhruvraj12
# }
# r2=requests.post(url=url,data=data)
#
# import requests
# import json
# def speak(str):
#
#     from win32com.client import Dispatch
#
#     speak=Dispatch("SAPI.SpVoice")
#
#     speak.Speak(str)
# if __name__ == '__main__':
#     speak('news for today')
#     url="https://newsapi.org/v2/top-headlines?country=us&apiKey=bb2be5e03d19493d9c14a81e51aadbbe"
#     news= requests.get(url).text
#     news_dict=json.loads(news)
#     print(news_dict['articles'])
#     arts=news_dict['articles']
#
#     for articles in arts:
#         speak(articles['title'])
#         speak('next news is')


# print(x.text)


# import win32api
#
# win32api.Beep(500, 3000)
# import win32api
#
# pos = (300, 200)
# win32api.SetCursorPos(pos)

import re

mystr = """Email:enquiry@alliance.edu.in   Helpline: +91 80 3093 8100 / 8200 / 4619 9100
 Media  Library  News  Webmail  Careers
 Alliance University
 Conferences
 Admissions Open
 Select Language
UPDATES:
ABOUT US 
WHY AU 
COLLEGES 
FACULTY
INTERNATIONAL PROGRAMS
PROGRAMS
RESEARCH
ADMISSIONS 
PLACEMENTS
CONTACT US
Contact UsHome Contact Us
 Contact Us Back
 Vice-Chancellor
Dr. Pavana Dibbur
 : vc@alliance.edu.in
 : +91 80 3093 8100/4619 9100

 Pro Vice-Chancellor (Academics, Research & Strategy)
Dr. Anubha Singh
 : anubha@alliance.edu.in
 : +91 80 3093 8102

 Registrar
Mr. Madhu Sudan Mishra
 : registrar@alliance.edu.in
 : +91 80 3093 8100/4619 9100

 Registrar (Examination & Evaluation)
Dr. Sajan Mathew
 : registrar.exams@alliance.edu.in
 : +91 80 3093 8141

 Director (Placements)
Mr. Mathew Thankachan
 : placement@alliance.edu.in | mathew.t@alliance.edu.in
 : +91 80 3093 8124 | 98444 72674

 Director (International Affairs)
Mr. Rajen Chatterjee
 : rajen.chatterjee@alliance.edu.in
 : +91 80 3093 8075

 Director (Admissions)
Mr. Abhay Chebbi
 : abhay.chebbi@alliance.edu.in
 : +91 96636 46464

 Human Resources Department
 : hrd@alliance.edu.in
 : +91 80 3093 8210 / 8204

 Student Verification 
Office of Registrar (Examination & Evaluation)
 : edu.verify@alliance.edu.in
 : +91 80 3093 8100 / 8200 | +91 80 4619 9100

 Contacts Info
 ALLIANCE UNIVERSITY
 Central Campus
Chikkahagade Cross, Chandapura - Anekal Main Road, Anekal
Bengaluru – 562 106, Karnataka,   India. [ Get Route Map ]
+91 80 3093 8100/8200/4619 9100 | Fax: +91 80 4619 9099
E-mail : enquiry@alliance.edu.in

 Office of Admissions
UG: +91 9620009825 | 91084 43123 | 91084 42143 | 98806 19618
PG: +91 98860 02500 | 99002 29974 | 90083 16363

 City Campus 1
19th Cross, 7th Main, BTM 2nd Stage, N.S. Palya
Bengaluru – 560 076, Karnataka,   India. [ Get Route Map ]
Tel.: +91 80 26786020 / 21 , 26789749

 City Campus 2
2nd Cross, 36th Main, Dollars Scheme, BTM 1st Stage
Bengaluru – 560 068, Karnataka,   India. [ Get Route Map ]
Tel.: +91 80 26681444 / 4372 | Fax: +91 80 26782048

 CONTACT INFO
 Contact Us
 Enquiry
 Feedback
 Get Route from Address
Quick Course Finder


Find Courses
 SCHOOLS | COLLEGES
 Alliance School of Business
 Alliance College of Engineering and Design
 Alliance School of Law
 Alliance Ascent College
 Planned Academic Units
International Partners

Antwerp Management School
Antwerp Management School"""

patt = re.findall("[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]+", mystr)
print(patt)
f = open("mylogs.txt", "w")
i=0
j=1
while True:
    f.writelines(f"email {j} = {patt[i]}\n")
    i+=1
    j+=1
f.close()
