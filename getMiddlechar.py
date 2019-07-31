def get_middle(s):

    char = list(s)
    indToPrint = int(len(char) / 2)

    if len(char) % 2 == 0 :
        return(char[indToPrint-1] + char[indToPrint])
    else:
        return(char[indToPrint])


"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
top Codewars solution
return s[(len(s)-1/2:len(s)/2+1
"""