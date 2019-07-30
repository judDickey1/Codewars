from string import ascii_letters

def find_missing_letter(chars):
    start = ascii_letters.index(chars[0])

    for char, match_char in zip(chars,ascii_letters[start:]):
        if char != match_char:
            return match_char