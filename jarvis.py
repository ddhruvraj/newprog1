# import pyttsx3
# import datetime
# import speech_recognition as sr
# import wikipedia
# import webbrowser
#
#
# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
#
#
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
#
# def wishme():
#     hour=datetime.datetime.now().hour
#     if hour>=0 or hour<12:
#         speak("good morning")
#     elif hour>=12 or hour<18:
#         speak("good afternoon")
#     else:
#         speak("good evening")
#     speak(f"hii i am jarvis how may i help you")
#
# def takecommand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print("listening...")
#         r.pause_threshold=1
#         audio=r.listen(source)
#     try:
#         print("Recognizing...")
#         query=r.recognize_google(audio,language='en-in')
#         print(f"user said: {query}")
#     except Exception as e:
#         print("say this again please")
#         return "none"
#     return query
# if __name__ == '__main__':
#     wishme()
#     while True:
#         query=takecommand().lower()
#         if 'wikipedia' in query:
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=2)
#             speak("According to Wikipedia")
#             print(results)
#             speak(results)
#         elif 'open youtube' in query:
#             webbrowser.open("youtube.com")

#
# import time
#
# import mouse
# import pyautogui
# import webbrowser
#
# pyautogui.alert('This is an alert box.')
# pyautogui.confirm('Shall I proceed?')
# pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
# pyautogui.prompt('What is your name?')

# if __name__ == '__main__':
#     n = int(input())
#     i=1
#     while i<=n:
#         print(i)
#         i+=1
# Replace all ______ with rjust, ljust or center.

# thickness = 5 #This must be an odd number
# c = '-'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
# n=int(input())
# k=97+n
#
# for i in range(k-1,96,-1):
#     print(chr(i),end="-")
# for i in range(98,k):
#     print(chr(i),end="-")
#
#
#
# def print_rangoli(size):
#     # your code goes here
#     k=97+n
#     # p=(size*2)
#     for i in range(k,122,-1):
#         print(chr(k).center(17,"-"))
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)
# s="hello world"
# list1 = s.split(" ")
# list3=[]
# print(list1)
# for i in list1:
#     print(i)
#     m=i.capitalize()
#     list3.append(m)
# print(list3)
# print(" ".join(list3))
# importing itertool module
# from itertools import product
# a=input().split(" ")
# b=input().split(" ")
# list3=[]
# list4=[]
# for i in range(len(a)):
#     A=list3.append(int(a[i]))
# for j in range(len(b)):
#     B=list4.append(int(b[j]))
#     # print(A,B)
# # a=[1,2]
# # b=[3,4]
# list1=list(product(list3,list4))
#
# for i in list1:
#     print(i,end=" ")
#


# print(' '.join([''.join(item) for item in result]))
# import itertools
# list1=[]
# from itertools import permutations
#
# for p in itertools.permutations("hack",2):
#     list1.append(list(p))
#
#
# # print(list1)
# list2=sorted(list1)
# # print(list2)
# for i in range(len(list2)):
#     for j in range(len(list2[i])):
#         if j%2==0:
#             print(list2[i][j],end="")
#         else:
#             print(list2[i][j])
#
#
import cmath
import itertools
# list1=[]
# str,b=input().split(" ")
# B=int(b)
# srt=sorted(str)
# # print(srt)
# for i in srt:
#     print(i)
# #
# comb=itertools.combinations(srt,2)
# for i in comb:
#     list1.append(list(i))
# # print(list1)
# temp=2-1
# for p in range(len(list1)):
#     for j in range(len(list1[p])):
#         if j==temp:
#             print(list1[p][j])
#             # temp+=B
#         else:
#             print(list1[p][j],end="")
#             # temp+=B

# Enter your code here. Read input from STDIN. Print output to STDOUT
# import cmath
# x,y=input().split("+")
# X=int(x)
# z=y.split("j")
# # print(z)
# z.pop()
# cp=int(z[0])
# # print(cp)
# print(abs(complex(real=X,imag=y)))
# phase=cmath.phase(complex(x,cp))
# print(phase)

# #
# print(abs(complex(1,2)))
# print(cmath.phase(complex(1,2)))


import collections
from collections import Counter
count=0
list=[]
var2=int(input())
var1=input().split(" ")
for j in range(len(var1)):
    xyz=int(var1[j])
    list.append(xyz)
# dict=Counter(list)
# print(dict)
for i in range(int(input())):
    var=input().split(" ")
    x1=int(var[0])
    x2=int(var[1])
    if x1 in list:
        list.remove(x1)
        count=count+x2
print(count)
