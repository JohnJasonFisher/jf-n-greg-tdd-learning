input_number = 12
#input_number = 7
#input_number = 62

pennies = 0
nickel = 0
dime = 0

while (input_number > 10):
    dime +=1
    input_number  -= 10

while (input_number > 5):
    nickel +=1
    input_number  -= 5

pennies = input_number

print(str(dime) + ' dimes, ' + str(nickel) + ' nickels, ' + str(pennies) + ' pennies')
