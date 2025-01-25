
def palindrome_func(word: str) -> bool:
    """
        Returns boolean, checking if the word is palindrome
        Arguments:
        word (type: str)
        We ignore case of letters
        We compare the text with its reversed version
    """
    if not isinstance(word, str):
        raise ValueError("The 'word' argument must be of type string (str)!")

    word = word.lower()
    return word == word[::-1]


# Testing function

print(palindrome_func("python"))  ### False
print(palindrome_func("Madam"))  ### True
print(palindrome_func("potop"))  ### True
print(palindrome_func(379))   ### ValueError



