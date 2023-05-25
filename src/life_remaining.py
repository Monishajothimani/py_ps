 #🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months
# print(type(age))

current_age = int(age)
living_age = 90 - current_age
# print(living_age)

days = living_age * 365
weeks = living_age * 52
month = living_age * 12
print(f"You have {days} days, {weeks} weeks, and {month} months left.")