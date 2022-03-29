"""
print("enter value 1=")
var1 = int(input())
print("enter value 2=")
var2 = int(input())
print("sum of entered values is=", var1 + var2)
print("subtaction of entered values is=", var1 - var2)
print("multiplication of entered values is=", var1 * var2)
print("divison of entered values is=", var1 / var2)
"""
# mystr="dhruv is good boy"
# print(len(mystr))
# print(mystr[::-1])

# numbers=[2,7,3,12,9]
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.pop()
# print(numbers)

# d1={"dhruv":"raj","raj":"dhruv","neel":"kumar","kumar":"neel"}
# print("enter your word=")
# str=input()
# print("meaning of your entered word is=",d1[str])

# print("enter your age(between 10 to 80)=")
# age=int(input())
#
# if 60>age>18:
#     print("you can drive car")
# elif age<18:
#     print("you can not drive car \n you are under age")
# elif age>60:
#     print("you can not drive car \n you are over age")
# elif age==18:
#     print("we can't decide \n please come phisicaly")
# else:
#     print("enter valid input")


# var1 = int(input("enter value 1="))
# var2 = int(input("enter value 2="))
# var3=int(input("which operation you want to perform(enter 1 for addition ,2 for subtraction,3 for multiplication,4 for divison)="))
#
#
# if var1==55 and var2==10 and var3==1:
#     print("45")
# elif var1 == 100 and var2 == 50 and var3 == 2:
#     print("150")
# elif var1 == 20 and var2 == 4 and var3 == 3:
#     print("90")
# elif var3== 1 :
#     print("sum of entered values is=", var1 + var2)
# elif var3==2:
#     print("subtaction of entered values is=", var1 - var2)
# elif var3 == 3:
#     print("multiplication of entered values is=", var1 * var2)
# elif var3 == 4:
#     print("divison of entered values is=", var1 / var2)


# list=["dhruv",34,"raj","neel",2,"kumar",7,9,3]
# for item in list:
#     if str(item).isnumeric() and item>6:
#         print(item)
# num=34
# num2=1
# num3=3
# print("you have only 3 chances")
# while (num2<4):
#
#         var=int(input("guess any number"))
#         if var>num:
#             print("your guess is greater")
#         elif var<num:
#             print("your guess is less")
#         else:
#             print("congrats you win")
#
#         num2=num2+1
#         num3=num3-1
#         if num3==0:
#             print("you loss the game")
#         elif num3>0:
#             print("you have",num3,"chances remaining")



# var=int(input("enter a value "))
# new=bool(var)
# if new==True:
#
#     n=1
#     m=1
#     while(n<5):
#        print(m*"*")
#        m=m+1
#        n=n+1
# elif new==False:
#
#     n=1
#     m=4
#     while(n<5):
#        print(m*"*")
#        m=m-1
#        n=n+1

# import random
# choice=random.randint(0,5)
# print(choice)
#
# import random
# no_of_chance=10
# chance=0
# list = ["snake", "water", "gun"]
#
# while chance<no_of_chance:
#     var = input("enter your choice(s for snake ,w for water and g for gun)")
#     rand=random.choice(list)
#     if var==rand:
#         print("same")
#
#     elif var=="s" and rand=="w":
#         print("you are win")
#     elif var=="s" and rand=="g":
#         print("you are loss")
#     elif var=="w" and rand=="s":
#         print("you are loss")
#     elif var=="w" and rand=="g":
#         print("you are win")
#     elif var=="g" and rand=="s":
#         print("you are win")
#     elif var=="g" and rand=="w":
#         print("you are loss")
#
#     chance=chance+1
# print("game over")

# Snake Water Gun Game
# import random
#
# print("Welcome to Snake, Water, Gun Game\n")
# print("Number of chances to play are only 10\n")
# print("Write s for snake,w for water,g for gun")
#
# chance = 10
# no_of_chance = 0
# AI_points = 0
# Player_points = 0
#
# while (no_of_chance < 10):
#
#     lst = ['snake', 'water', 'gun']
#     r = random.choice(lst)
#     inp = int(input("Snake Water Gun:\n"))
#     print(r)
#
#     # inp=snake r=water
#     if inp == "s" and r == "water":
#         Player_points = Player_points + 1
#         print("You won! Snake ne pani pi liya")
#         print(f"player points are {Player_points} and computer points are{AI_points}")
#
#     # inp=snake r=gun
#     if inp == "s" and r == "gun":
#         AI_points = AI_points + 1
#         print("You Lose! Gun killed snake")
#         print(f"player points are {Player_points} and computer points are{AI_points}")
#
#     # inp=r Tie
#     if inp == "s" and r == "snake":
#         print("Tie")
#         print(f"Player points are {Player_points} and computer points are{AI_points}")
#
#     # Inp=water r=gun
#     elif inp == "w" and r == "gun":
#         Player_points = Player_points + 1
#         print("You won! Gun pani mein dub gayi")
#         print(f"player points are {Player_points} and computer points are{AI_points}")
#
#     # Inp=water r=snake
#     elif inp == "w" and r == "snake":
#         AI_points = AI_points + 1
#         print("You Lose! Snake ne pani pi liya")
#         print(f"player points are {Player_points} and computer points are{AI_points}")
#
#     # Inp=gun r=snake
#     elif inp == "g" and r == "snake":
#         Player_points = Player_points + 1
#         print("You Won! Gun killed snake")
#         print(f"player points are {Player_points} and computer points are{AI_points}")
#
#     # Inp=gun r=water
#     elif inp == "g" and r == "water":
#         AI_points = AI_points + 1
#         print("You Lose! Gun pani mein dub gayi")
#         print(f"player points are {Player_points} and computer points are{AI_points}")
#
#     no_of_chance = no_of_chance + 1
#     print(f"{chance - no_of_chance} is left out of {chance}")
#
#     if AI_points < Player_points:
#         print(f"You won from computer by", Player_points - AI_points, "points")
#
#     if AI_points > Player_points:
#         print(f"You Lose! computer won by", AI_points - Player_points, "points")
#
#     if AI_points == Player_points:
#         print("Match Tie")
#
#     elif inp > 3:
#         print("Invalid input! Please check it")
#
#
# import random
# choice=0
# com_point=0
# user_point=0
# chance=11
# print("snake,water,gun game")
# print("you can play this game 10 times")
# print("press s for snake \n w for water \n g for gun")
# list=["snake","water","gun"]
# while(choice<11):
#     chance=chance-1
#     inp=input()
#     r=random.choice(list)
#     #if input and random is same
#     if inp=="s" and r=="snake":
#         print("match is tie")
#         print(f"you have {chance} remaining")
#     if inp=="w" and r=="water":
#         print("match is tie")
#         print(f"you have {chance} remaining")
#     if inp=="g" and r=="gun":
#         print("match is tie")
#         print(f"you have {chance} remaining")
#     #input=snake and random=water
#     elif inp=="s" and r=="water":
#         print("you are win")
#         user_point=user_point+1
#         print(f"your choice is {inp} and computer's choice is {r} \n your points are {user_point} and computer's points are {com_point} \n you have {chance} chances remaining")
#     #input=snake and random=gun
#     elif inp == "s" and r == "gun":
#         print("you are loss")
#         com_point = com_point + 1
#         print(f"your choice is {inp} and computer's choice is {r} \n your points are {user_point} and computer's points are {com_point} \n you have {chance} chances remaining")
#     #input=water and random=gun
#     elif inp == "w" and r == "gun":
#         print("you are win")
#         user_point = user_point + 1
#         print(f"your choice is {inp} and computer's choice is {r} \n your points are {user_point} and computer's points are {com_point} \n you have {chance} chances remaining")
#     #input=water and random=snake
#     elif inp == "w" and r == "snake":
#         print("you are loss")
#         com_point = com_point + 1
#         print(f"your choice is {inp} and computer's choice is {r} \n your points are {user_point} and computer's points are {com_point} \n you have {chance} chances remaining")
#     # input=gun and random=water
#     elif inp == "g" and r == "water":
#         print("you are loss")
#         com_point = com_point + 1
#         print(f"your choice is {inp} and computer's choice is {r} \n your points are {user_point} and computer's points are {com_point} \n you have {chance} chances remaining")
#     elif inp == "g" and r == "snake":
#         print("you are win")
#         user_point = user_point + 1
#         print( f"your choice is {inp} and computer's choice is {r} \n your points are {user_point} and computer's points are {com_point} \n you have {chance} chances remaining")
#     choice=choice+1

#
# import datetime
# tday=datetime.date.today()
# print(tday)
#
# tdelta=datetime.timedelta(days=7)
# print(tday+tdelta)
# print(tday-2*tdelta)
#
#
# bday=datetime.date(2022,7,13)
# till_bday=bday-tday
# print(till_bday)
#
# t=datetime.time(8,32,12,1234)
# print(t.hour)

# import datetime
# t=datetime.timedelta(minutes=1)
# nt=datetime.datetime.now()
# k=datetime.time(10,25,0,0)
# # v=datetime.timedelta(seconds=1)
# print(nt)
# # print(nt+t)
#
# while nt!=k:
#     print("hi")
#
#     nt+t

# class employee:
#     leave_of_employee=8
#     pass
#
#     def printdetails(self):
#         return f" name is {self.name} and salary is {self.salary} \n role is {self.role}"
#
#     def __init__(self,aname,asalary,arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#
#
#
# dhruv=employee("dhruv",1234,"faculty")
# raj=employee("raj",2345,"student")
#
#
# # dhruv.name="dhruv"
# # dhruv.salary=1234
# # dhruv.role="faculty"
# # raj.name="raj"
# # raj.salary=2345
# # raj.role="student"
#
# # print(employee.leave_of_employee)
# # print(employee.__dict__)
# # employee.leave_of_employee=9
# # print(employee.__dict__)
# # print(employee.leave_of_employee)
# print(dhruv.printdetails())

dict={'a':1,'b':2}
print(list(dict)[0])
