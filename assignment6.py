# my assignment 
"""calculator with functions """

#functions
#1.addition function (simple function)
def add():
    x=int(input("please enter your first number: "))
    y=int(input("please enter your second number: "))
    print("addition is : ",x+y)

#2.subtraction function with arguments without return type
def subtract(x,y):
    print(f"subtraction of {x} and {y} is : ",x-y)

#3.multiplication function without argument with return type 
def mul():
    x = int(input("please enter your first number: "))
    y=int(input("please enter your second number: "))
    return x*y  


#4.division function with argument with return type 
def div(x,y):
    return x/y

#5.modulus function with argument without return type
def mod(x,y):
    print("mod is :",x%y)

#6.exponent multiplication function with argumets with return type
def expmul(x,y):
    return x**y
   

#7. exponent division funtion with argument with return type
def expdiv(x,y):
    return x//y



while True:
    print("press 1 for addition ")
    print("press 2 for subtraction")
    print("press 3 for muliplication")
    print("press 4 for division")
    print("press 5 for modulus")
    print("press 6 for  exponent modulus")
    print("press 7 for exponent division")
    print("press 8 to exit")
    choice=input()
    if choice == '1':
        add()

    elif choice=='2':
        x=int(input("please enter your first number: "))
        y=int(input("please enter your second number: ")) 
        if x>=y:
            subtract(x,y)
        else :
            subtract(y,x) 
    elif choice=='3':
        print(mul()) 
    elif choice=='4':
        x=int(input("please enter your first number: "))
        y=int(input("please enter your second number: ")) 
        print(div(x,y))
    elif choice=='5':
        x=int(input("please enter your first number: "))
        y=int(input("please enter your second number: "))   
        mod(x,y)  
    elif choice=='6':
        x=int(input("please enter your first number: "))
        y=int(input("please enter your second number: ")) 
        print(expmul(x,y))
    elif choice=='7':
        x=int(input("please enter your first number: "))
        y=int(input("please enter your second number: ")) 
        print(expdiv(x,y))
    elif choice=='8':
     break       
    else:
      print("please enter a valid choice")    