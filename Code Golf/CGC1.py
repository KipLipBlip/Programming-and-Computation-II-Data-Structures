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
    x,y,i='',len(s),0
    while i!=y:
        if s[i].isupper() or not s[i].isalnum(): x,i=x+s[i],i+1
        else: 
            x+='"'
            while i!=y and s[i].islower(): x,i=x+s[i],i+1
            x+='"'
    return x

    #while n<1000: rn += n if not (n % 3 and n % 5) else 0 || add n to rn if the condition holds, else add 0

if __name__ == "__main__":

    import doctest
    doctest.testmod()

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