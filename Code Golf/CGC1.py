def addQuotes(s):
    '''
        *Write a function that adds double quotes around lowercase words
        *A "lowercase word" is defined as a sequence of lowercase characters
        *Type checking is not required. All inputs will be a string.
        *Function name must be addQuotes, and it must take exactly one parameter (input string).
            Example: def addQuotes(inputString):

        Doctest:
            >>> addQuotes('[[one, two, three]')
            '[["one", "two", "three"]'
            >>> addQuotes('this is a test')
            '"this" "is" "a" "test"'
            >>> addQuotes('test')
            '"test"'
            >>> print(addQuotes("""this "one" "contains' "quotations"""))
            "this" ""one"" ""contains"' ""quotations"
            >>> addQuotes('Hello  SpeciaL!')
            'H"ello"  S"pecia"L!'
            >>> addQuotes('NO CHANGE')
            'NO CHANGE'
            >>> addQuotes('')
            ''
    '''
    y=''
    for i in range(len(s)):
        x=''
        z=''
        if s[i].islower():
            while s[i].islower():
                z+=s[i]
                i+=1
            x+='"'+z+'"'
        else:
            x+=s[i]
        y+=x

    return y

    # x=lambda s: [[] if [if s[i].islower() for j in range(len(s))] else s for i in range(len(s)) ]
    # return x

if __name__ == "__main__":

    import doctest
    doctest.testmod()
