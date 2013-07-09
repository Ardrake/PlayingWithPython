# execfile("./Study/strings.py")

funstring = "Test sentence again again again again again "
funstring = """It takes into account the case when the vowels are in either uppercase or lowercase. It might not be the most efficient way to traverse recursively a string (because each recursive call creates a new sliced string) but it's easy to understand:


Base case: if the string is empty, then it has zero vowels.
Recursive step: if the first character is a vowel add 1 to the solution, otherwise add 0. Either way, advance the recursion by removing the first character and continue traversing the rest of the string.
The second step will eventually reduce the string to zero length, therefore ending the recursion. Alternatively, the same procedure can be implemented using tail recursion - not that it makes any difference regarding performance, given that CPython doesn't implement tail recursion elimination."""
funstring = "   This is a test of the emergency    "

def countWords(words, subj):
    if not words:
        return 0
    else:
        return (1 if words[0] == subj else 0) + countWords(words[1:], subj)


# reverse a list in place
#" ".join(TEXT.split()[::-1])

def StripWhitespaceI(str):
    i = 0
    j = len(str)-1
    
    while i < j:
        if str[i] == " ":
            str = str[1:]
            j -= 1
        else:
            i += 1
        if str[j] == " ":
            str[j] = str[0:-1]
        else:
            j -= 1

    return str

def StripWhitespaceR(str):
    if str[0] != " " and str[len(str)-1] != " ":
        return str
    else:
        if str[0] == " ":
            return StripWhitespace(str[1:])
        if str[len(str)-1] == " ":
            return StripWhitespace(str[0:len(str)-1])
