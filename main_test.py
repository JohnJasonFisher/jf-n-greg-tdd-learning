from main import return_big_coins

expected_message = '1 nickels, 2 pennies'
actual_message = return_big_coins(7)

if (actual_message == expected_message):
    print('Is correct')
else:
    print('Is incorrect')

expected_message = '1 dimes, 2 pennies'
actual_message = return_big_coins(12)

if (actual_message == expected_message):
    print('Is correct')
else:
    print('Is incorrect')
