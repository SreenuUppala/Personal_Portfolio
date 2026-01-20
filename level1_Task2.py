temp = float(input("Enter Temperature With Celsius or Fahrenheit:"))
units = input("Enter Units C for Celsius or F for Fahrenheit:").upper()
if units == 'C':
    convert = (temp * 9 / 5) + 32
    print(f"{temp}°C is equal to {convert}°F")
elif units == 'F':
    convert = (temp - 32) * 5 / 9
    print(f"{temp}°F is equal to {convert}°C")
else:
     print("you are enter invalid units")
