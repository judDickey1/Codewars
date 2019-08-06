'''
A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base.
For example, take 153 (3 digits):
 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
 Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.
'''

def narcissistic(value):
    valuestring = str(value)
    sum = 0
    intList = [int(x) for x in valuestring]
    for x in intList:
       sum += (x ** len(intList))

    return sum == value


if __name__ == '__main__':
    print(narcissistic(153))
    print(narcissistic(1634))

'''
Top CodeWars Solution
def narcissistic(value):
return value == sum(int(x) ** len(str(value)) for x in str(value))
'''