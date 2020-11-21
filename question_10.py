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
