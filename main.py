def return_big_coins(input_number):
    pennies = 0
    nickel = 0
    dime = 0

    while (input_number >= 10):
        dime +=1
        input_number  -= 10

    while (input_number >= 5):
        nickel +=1
        input_number  -= 5

    pennies = input_number

    return (str(dime) + ' dimes, ' + str(nickel) + ' nickels, ' + str(pennies) + ' pennies')

if (__name__ == '__main__'):
    print(return_big_coins(7))
    print(return_big_coins(12))
    print(return_big_coins(27))
    print(return_big_coins(62))
