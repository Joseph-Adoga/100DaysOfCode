#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

tip_calculated = bill * (tip_percentage / 100)
total_bill = bill + tip_calculated
bill_split = total_bill / number_of_people
bill_split_rounded = round(bill_split, 2)
bill_split_rounded = "{:.2f}".format(bill_split_rounded)
print(f"Each person should pay: ${bill_split_rounded}")

#Day 2
#Tip Calculator
#100DaysOfCode
#Angela Yu
#Joseph Adoga