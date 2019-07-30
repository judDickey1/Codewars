##codewars top soln
#return len(string) == len(set(string.lower()))

##my soln
def is_isogram(string):

    this_string = string.lower()
    mylist = []

    for letter in this_string:

        if letter.isalpha():

            if (letter in mylist):
                return False
            mylist.append(letter)
    print(mylist)
    return True

if __name__ == '__main__':
    print(is_isogram("Machine"))
    print(is_isogram("isogram"))
    print(is_isogram("GeeksforGeeks"))
    print(is_isogram("Alphabet "))