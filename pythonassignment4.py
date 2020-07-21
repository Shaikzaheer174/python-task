#assignment
"""
 create a login page same as gmail.. their should be 6 users ,with the nested if conditinal statement
 """
user1="zaheer"
user2="soumi"
user3="rakesh"
user4="chinmay"
user5="saikiran"
user6="roshan"

pass1="zaheer1"
pass2="soumi1"
pass3="rakesh1"
pass4="chinmay1"
pass5="saikiran1"
pass6="roshan1"


username=input("hey,please enter your username : ")
if username == user1:
    password=input(f"hey{username} please enter your password")
    if password==pass1:
        print(f"hello {username} you are logged in")
    else:
        print("sorry,the password you entered is incorrect")  

elif username == user2:
    password=input(f"hey {username} please enter your password :")
    if password==pass2:
         print(f"hello {username} you are logged in")
    else:
        print("sorry, the password you entered is incorrect")

elif username == user3:
    password=input(f"hey{username} please enter your password")
    if password==pass3:
         print(f"hello {username} you are logged in")
    else:
        print("sorry, the password you entered is incorrect")
        
elif username == user4:
    password=input(f"hey{username} please enter your password")
    if password==pass4:
         print(f"hello {username} you are logged in")
    else:
        print("sorry, the password you entered is incorrect")
        
elif username == user5:
    password=input(f"hey{username} please enter your password")
    if password==pass5:
         print(f"hello {username} you are logged in")
    else:
        print("sorry, the password you entered is incorrect ")
        
elif username == user6:
    password=input(f"hey{username} please enter your password")
    if password==pass6:
         print(f"hello {username} you are logged in")
    else:
        print("sorry, the password you entered is incorrect ")
        
else:
    print("you are not a valid user so,please enter a valid username ")