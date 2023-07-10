from main import return_big_coins

if (return_big_coins(7) == '1 nickels, 2 pennies'):
    print(return_big_coins(7) + ' is correct')
else:
    print(return_big_coins(7) + ' is incorrect')

if (return_big_coins(12) == '1 dimes, 2 pennies'):
    print(return_big_coins(12) + ' is correct')
else:
    print(return_big_coins(12) + ' is incorrect')
