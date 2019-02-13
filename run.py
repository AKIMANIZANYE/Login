#!/usr/bin/env python3.6
from sigin import User

U=input("username : ")
print("create  password")
P=input("password : ")
save = User(U, P)
save.saving()
print("Username and password has been created !!!")

print("Welcome again login into your acount")


    #this  will check the created account

def main():
    print("Hello Welcome to your contact list. What is your name?")
          
    while True:
        print("Use these short codes : cc - create a newusername and password, dc - for delete the account, fc -find a username, ex -exit the username list ")
        short_code = input().lower()

        if short_code == 'cc':
            usr=input() #for username
            print("enter your password")
            passd=input()#for password       
            if(save.username==usr and save.password==passd):
                print("Deleting  was succesully")
            else:
                print("username or password incorrect")
                            

        elif short_code == 'dc':
            
            User.user_list.remove(save)
            print("login succesully")

                        
        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")

main()