empname=["amam","preet","singh"]
ids=[147,258,369]
amount=[1400,2000,6500]

for i in range(7000):
    choice=int(input("enter your id number : "))
    if choice in ids:
      for i in range(len(ids)):
          if choice==ids[i]:
              print( empname[i], " your amount is ",amount[i])
    else:
        print("please enter a valid id")     
        break
    


    