#roller coaster ride#
height = int(input("what is your height ?"))


if(height>=120):
    print("allowed for ride.")

    age = int(input("What is your age ?"))

    bill = 0
    if(age<12):
        bill+=5
    elif(age<18):
        bill+=7
    elif(age<45):
        bill+=12
    elif(age>=45 and age<=55):
        bill = 0
    photos = input("want photos? Y or N")
    if(photos =="Y"):
        bill+=3
        
    print(f"the total bill is : $ {bill}")
else:
    print("not allowed for ride.")