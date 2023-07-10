input_number = 12

pennies = 0
nickel = 0
# dime = 0

while (input_number > 5):
    nickel +=1
    input_number  -= 5

pennies = input_number

print(str(nickel) + ' nickel, ' + str(pennies) + ' pennies')
