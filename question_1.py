# Question 1:

# Two friends are eating dinner at a restaurant. 
# The bill comes in the amount of 47.28 dollars. 
# The friends decide to split the bill evenly between them, 
# after adding 15% tip for the service. 
# Calculate the tip, the total amount to pay, and each friend's share, 
# then output a message saying "Each person needs to pay: " 
# followed by the resulting number.

bill = 47.28
tip = bill * (15/100) # finding how much the tip is = $7.092
total = bill + tip # 47.28 + 7.092 = 54.372
share = total/2 # 54.372 / 2 = 27.19
print("Each person needs to pay: " + str(share))
