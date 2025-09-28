'''
Name: Ricky Berliant
Date: 10/05/2025
Class: ISTA 130
Section Leader: Sungjoon Shin
'''

# ISTA 130 Extra Credit Worksheet Week 6
# 1.) Write a Boolean expression that evaluates to True if the value of the variable count is between 1 and 10 inclusive.

count = 0
if 1 <= count <= 10:
    print(True)
else:
    print(False)


# 2.) How does Python know to which if an else belongs? 

'As for example in this:'

'''
if name == "Snoopy":
    if color == "white":
        print("Yep, Snoopy")
    else:
        print("Nope, imposter")
'''

'''
Python determines which if an else belongs to by indentation. 
An else is paired with the most recent if at the same indentation level. 
The else is indented under if color == "white":, 
so it only executes if the color is not "white" and the name is "Snoopy".
'''


# 3.) Write a conditional statement that sets the  
# value of a variable named answer to 1 if a variable named result
# is equal to 100. Set answer to 2 otherwise.

result = 100

if result == 100:
    answer = 1
else:
    answer = 2

# 4.) Write a conditional statement that sets the value of a variable gradepoint to 4 
# if a variable named score is 90 or above, 3 if score is at least 80 and less than 90, 
# 2 if score is at least 70 and less than 80, 
# 1 if score is at least 60 and less than
# 70, and 0 otherwise.

score = 100

if score >= 90:
    grade_point = 4
elif score >= 80:
    grade_point = 3
elif score >= 70:
    grade_point = 2
elif score >= 60:
    grade_point = 1    
else:
    grade_point = 0
    

# 5.) 
# A fruit company sells oranges for 32 cents a pound plus $7.50 per order for shipping. If an order is over 100 pounds, shipping
# cost is reduced by $1.50. Write a function that will take the number of pounds of oranges as a parameter and return the
# cost of the order.

def fruit_company(num_pound_oranges):
    cost = num_pound_oranges * 0.32
    per_order_shipping = 7.50

    if num_pound_oranges > 100:
        per_order_shipping -= 1.50
        
    total_cost = cost + per_order_shipping
        
    return total_cost


# 6.) Write a function that takes three integers as parameters and returns the largest.

def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b 
    else:
        return c



# 7.) Write a function that takes two parameters, 
# a pay rate and the number of hours worked, and returns the pay.
# Any hours over 40 are paid at time and a half.


def hourly_pay(pay_rate, num_of_hours):
    if num_of_hours <= 40:
        pay = pay_rate * num_of_hours
    else:
        pay = (40 * pay_rate) + ((num_of_hours - 40) * pay_rate * 1.5)
    return pay


def main():
    print(largest_number(20, 64, 9000))
    print(hourly_pay(20, 45))
    print(fruit_company(150))
    

if __name__ == '__main__':
    main()



# 8.) What is the output of the following code?
weight_oz = 1.5 
length = 28

if weight_oz <= 1.0:
    price = 0.45 #False
elif weight_oz <= 2.0:
    price = 0.65 #True 
else: #False
    price = 1.05

#currently at price = 0.65
if length > 10:
    price = price + 0.25 #True (0.65 + .25 = .90)
if length > 20:
    price = price + 0.50 #True (.90 + .50 = 1.4)
if length > 30:
    price = price + 1.00 #False
print("Price is: $", str(price)) # $1.40

# Answer: $1.40

