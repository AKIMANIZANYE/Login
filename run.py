#!/usr/bin/env python3.6
from sigin import User
#This is for creating username  and password
print(" Welcome to the  world of program !! create an username and password")
print("what is your useranme")
U=input("username : ")
print("create  password")
P=input("password : ")
print("Username and password has been created !!!")

print("Welcome again login into your acount")
print("enter your username and password")
save = User(U, P)
save.saving()
det=(U,P)
model=input()
# loss = model(input(""))
# loss, something_else = model(input)
# det.test_delete()

    #this  will check the created account
usr=input() #for username
print("enter your password")
passd=input()#for password       
if(U==usr and P==passd):
    print("login succesully")
else:
    print("username or password incorrect")
