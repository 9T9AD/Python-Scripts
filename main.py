# Question 1:

# Two friends are eating dinner at a restaurant. 
# The bill comes in the amount of 47.28 dollars. 
# The friends decide to split the bill evenly between them, 
# after adding 15% tip for the service. 
# Calculate the tip, the total amount to pay, and each friend's share, 
# then output a message saying "Each person needs to pay: " 
# followed by the resulting number.

bill = 47.28
tip = bill * (15/100) 
total = bill + tip
share = total/2 
print("Each person needs to pay: " + str(share))



# Question 2:

#Combine the variables to display the sentence
# "How do you like Python so far?"

word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1+ ' ' + word2 + ' ' + word3 + ' '+ word4 + ' '+ word5 + ' '+ word6 + ' ' + word7 )



#Question 3:

# Put “This is fun!” onto the screen 5 times.

for i in range(5):
  print("This is fun!")



# Question 4:

# Replace the ___ placeholder and calculate the Golden ratio: 1 + √5 / 2
ratio = (1+(5**(1/2)))/2
print(ratio)
# To calculate the square root of a number x, you can use x**(1/2).



# Question 5

# This function converts miles to kilometers (km).
# - Complete the function to return the result of the conversion
# - Call the function to convert the trip distance from miles to kilometers
# - Fill in the blank to print the result of the conversion
# - Calculate the round-trip in kilometers by doubling the result, 
#   and fill in the blank to print the result.

#Answer: 

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(55)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km + my_trip_km))



# Question 7

# Let's revisit our lucky_number function. 
# We want to change it, so that instead of printing the message, 
# it returns the message. This way, the calling line can print the message, 
# or do something else with it if needed. 
# Fill in the blanks to complete the code to make it work.

def lucky_number(name):
  number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  return message
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))



# Question 8

# Flesh out the body of the print_seconds function 
# so that it prints the total amount of seconds
# given the hours, minutes, and seconds function parameters.
# Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

def print_seconds(hours, minutes, seconds):
    print(hours * 3600 + minutes * 60 + seconds)

print_seconds(1,2,3)



# Question 9

# Use the get_seconds function to work out the amount
# of seconds in 2 hours and 30 minutes, 
# then add this number to the amount of
# seconds in 45 minutes and 15 seconds. 
# Then print the result.

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)



# Question 10

# Use the function to convert 5000 seconds
# hours, minutes, seconds

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, seconds

time = convert_seconds(5000)
print(time)



#Question 11

# In this code, identify the repeated pattern and replace it with a function called month_days, that receives the name of the month and the number of days in that month as parameters. Adapt the rest of the code so that the result is the same. Confirm your results by making a function call with the correct parameters for both months listed

## REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")

# My code for the above question
def month_days(month,days):
    print(month + " has " + str(days) + " days")
    
month_days('July', 31)
month_days('June', 30)
