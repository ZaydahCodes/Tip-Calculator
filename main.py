#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60



print("welcome to the tip calculator")
total_bill =float(input("what is the total bill:"))
tip = int(input("What percentage tip would you like to give ? 10,12 or 15%?:"))
number_of_people = int(input("How many people to split the bill?:"))

bill =round((total_bill * (1 + tip /100)) / number_of_people,2)

print(f"Each person sould pay : {bill}")
