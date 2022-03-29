# ex 1
#
# var=input("enter 1 for know your age in perticular year \n"
#           "enter 2 for know when you complete your 100 years")
# if var=="1":
#     x=int(input("enter your age :"))
#     y=int(input("enter year (program show your age in entered year):"))
#     if x>=100 or x<=0 or y>=2125 or  y<=1900:
#         print("invalid input!")
#     else:
#         print(f"your current age is {x} and your age in {y} is {y-2022+x}")
# elif var=="2":
#     age=input("enter your age or year of birth:")
#     if age<="0":
#         print("invalid age ! \nplease enter valid age or year of birth")
#     elif len(age)==2:
#         print(f"you complete your 100 years after {100-int(age)} years in {2022+100-int(age)}")
#     elif len(age)==3:
#         print(f"you completed your 100 years before {int(age)-100} years in 2122")
#     elif age>="2023" :
#         print("you are not yet born")
#     elif len(age)==4:
#         print(f"you are {2022-int(age)} years old and you complete your 100 years in {int(age)+100}")
# else:
#     print("invalid input!")

# ex2

# n = int(input("enter number of apples dhruv have:"))
# mn = int(input("enter minimum childrens for give apples"))
# mx = int(input("enter maximum childrens for give apples"))+1
# while True:
#     if mn == mx:
#         break
#     elif n%mn == 0:
#         print(f"dhruv can distribute {n} apples to {mn} childs")
#     elif n%mn!=0:
#         print(f"dhruv can't distribute {n} apples to {mn} childs because {mn} is not divisor of {n}")
#     mn += 1

# ex3
# list12 = ["hii", "hello", "how", "are", "you"]
# first method
# list.reverse()   #for reverse without change original list
# reverse=list[:] this is make a copy means you can use reverse any where
# reverse.reverse()
# print("with first method(inbulit reverse function) reverse the list \n",list)
# second method(slicing list)
# list1=list[::-1]
# print("with second method reverse the list \n",list1)
# if a string is given
# a = list.index("hii")
# b = list.index("you")
# list[a], list[b] = list[b], list[a]
# c = list.index("hello")
# d = list.index("are")
# list[c], list[d] = list[d], list[c]
# print(list)
# user input string
# listlen=int(input("enter list length"))
# list12=[]
# for i in range(listlen):
#     list12.append(int(input("enter element")))
# print(f"your list is {list12}")
# reverse3=list12[:]
# for i in range(listlen//2):
#     reverse3[i],reverse3[len(reverse3)-i-1]=reverse3[len(reverse3)-i-1],reverse3[i]
# print(f"you reversed list is {reverse3}")
# ex4
# num = input("enter number")
# reverse = ''.join(reversed(num))
# print('The reverse number is =', reverse)
# if num == reverse:
#     print("entered number is palindrom")
# else:
#     print("entered number in not palindrom")
# while num != reverse:
#     int(num)=o
#     o+=1
# else:
#     print(f"Next palindrom number is {num}")
# ex7
# list = ["dhruv is is good boy", "this is python", "my name is dhruvraj", "hello how are you", "python is easy language",
#         "python is not python snake"]
# a = input("enter a query string which you want to find :")
# rev = a[:]
# j = 0
# k = 1
# m = 0
# # if a in list[i]:
# #     print("yes")
# #     i+=1
# for i in range(len(list)):
#     if a in list[j]:
#         print(f"{k} {list[j]}")
#         word = list[j].split()
#         for i in range(len(word)):
#             if a == word[m]:
#                 print("andar hain")
#             # else:
#             #     print("andar nahi hain")
#                 m += 1
#         k += 1
#     j += 1

# from collections import OrderedDict
#
# dict = {}
#
# for z in range(int(input())):
#     dict.update({input():int(input())})
#     new_dict=OrderedDict(dict)
#     print(new_dict.keys())
#     str=list(new_dict)[z]
#     m=new_dict.get(str)
#     x1=list(new_dict.keys())
#     print(len(x1))
#     i=0
#     m1=new_dict.get(str)
#     for k in range(len(x1)):
#         if str==x1[k]:
#             print("yes")
#             M=m1+m
#             print(M)
#             new_dict.update({str:M})
#         else:
#             i+=1
#
#     print(i)
#     print(new_dict)
#
#
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    var=input().split(" ")

    if var[0]=="pop":
        s.pop()
    elif var[0]=="remove":
        s.remove(int(var[1]))
    elif var[0]=="discard":
        s.discard(int(var[1]))
print(sum())