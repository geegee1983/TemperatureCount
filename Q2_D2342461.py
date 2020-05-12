# Problem: Determine the highest temperature in the list

# Input: temperatures
temperatures = [-3, -3, -3, -2, -2]

# Calculate the maximum temperature in the list
maximumTemperature = temperatures[0]

for temperature in temperatures:
    if temperature > maximumTemperature:
        maximumTemperature = temperature

# Count how many times the highest temperature occurs
count=0

for temperature in temperatures:
    if temperature == maximumTemperature:
        count = count+1

print("The maximum temperature occurs ", count, " number of times.")

