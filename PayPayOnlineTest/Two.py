import sys


def change_machine(change, change_list):
    change = float("{0:.2f}".format(change, change_list))
    if (change <= 0.0):
        return change_list
    elif (change >= 100):
        while (change >= 100):
            change -= 100
        change_list.append('ONE HUNDRED')
        return change_machine(change, change_list)
    elif (change >= 50):
        while (change >= 50):
            change -= 50
        change_list.append('FIFTY')
        return change_machine(change, change_list)
    elif (change >= 20):
        while (change >= 20):
            change -= 20
        change_list.append('TWENTY')
        return change_machine(change, change_list)
    elif (change >= 10):
        while (change >= 10):
            change -= 10
        change_list.append('TEN')
        return change_machine(change, change_list)
    elif (change >= 5):
        while (change >= 5):
            change -= 5
        change_list.append('FIVE')
        return change_machine(change, change_list)
    elif (change >= 2):
        while (change >= 2):
            change -= 2
        change_list.append('TWO')
        return change_machine(change, change_list)
    elif (change >= 1):
        while (change >= 1):
            change -= 1
        change_list.append('ONE')
        return change_machine(change, change_list)
    elif (change >= 0.5):
        while (change >= .5):
            change -= 0.5
        change_list.append('HALF DOLLAR')
        return change_machine(change, change_list)
    elif (change >= 0.25):
        while (change >= .25):
            change -= 0.25
        change_list.append('QUARTER')
        return change_machine(change, change_list)
    elif (change >= 0.10):
        while (change >= .10):
            change -= 0.10
        change_list.append('DIME')
        return change_machine(change, change_list)
    elif (change >= 0.05):
        while (change >= .05):
            change -= 0.05
        change_list.append('NICKEL')
        return change_machine(change, change_list)
    elif (change >= 0.01):
        while (change >= .01):
            change -= 0.01
        change_list.append('PENNY')
        return change_machine(change, change_list)


def stringify_currencies(currency_values):
    currency_values_string = ''
    for i in range(len(currency_values)):
        if len(currency_values_string) == 0:
            currency_values_string = currency_values_string + currency_values[i]
        else:
            currency_values_string = currency_values_string + ',' + currency_values[i]
    return currency_values_string


# for line in sys.stdin:
    # use default values
line = '15.94;16.58'
line_list = line.split(";")
purchase_price = float(line_list[0])
payment = float(line_list[1])

if payment < purchase_price:
    print('ERROR')
elif payment == purchase_price:
    print('ZERO')

change = float(payment - purchase_price)

change_list = []
currency_values = sorted(change_machine(change, change_list))
currency_values_string = stringify_currencies(currency_values)

print(currency_values_string)
