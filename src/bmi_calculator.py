# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(type(height))

height_1= float(height) 
weight_1 = int(weight)

#print(type(height_1))
#print(type(weight_1))


BMI = weight_1/(height_1**2)
#print(BMI)

BMI_Result = int(BMI)
print(BMI_Result)