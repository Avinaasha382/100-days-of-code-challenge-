# Day 2: I learnt more on data types, typecasting strings to other data types,  f -strings, arithmetic operations in python and practised
#        questions too.  

#   I also made a tip calculator as "Project of the day"

# tip calculator:


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)




print(f"Each person should pay: ${final_amount}") \


#BMI Calculator:

height = input()
weight = input()

h=float(height)
w=float(weight)
bmi=w/(h**2)
res=int(bmi)
print(res) 


# Life in weeks:

age = input()

left=90-int(age)

res=left*52
print(f"You have {res} weeks left.")



