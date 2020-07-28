
#function to get unique vlaue

names = []
n = 0
while n<10 :
    a=input("please enter your name :")
    if a not in names :
        names.append(a) 
        n+=1

    else :
        print("this name is already exist, please enter a new name : ")    

print(names)        