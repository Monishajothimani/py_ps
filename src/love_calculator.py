#Love calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = (name1 + name2)
lower_name = name.lower()
# print(lower_name)


t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e= lower_name.count("e")

sum_1 = t + r + u + e
# print(sum_1)
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e= lower_name.count("e")

sum_2 = l + o + v + e

score = str(sum_1) + str(sum_2)
total = int(score)

# print (f"Your score is {total}.")

if(total<10 or total>90):
    print(f"Your score is {total},"" you go together like coke and mentos.")
elif(total>40 and total<50):
    print(f"Your score is {total},"" you are alright together.")
else:
    print (f"Your score is {total}.")