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

# Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

def print_seconds(hours, minutes, seconds):
    print(hours * 3600 + minutes * 60 + seconds)

print_seconds(1,2,3)