def countOdd(aList):
    '''
        1. Modify the function countOdd so it returns the message Error if the input provided is not a list.
        If the input provided is a list, it must check only integers, which can be also represented as strings.
        To prove your  code  meets  the  requirements  write  the  tests  cases  in  the  file  test_odd.py. 
        Remember that unittest can help you perform tests in a bulk. Use it to your advantage!

        2. Modify the function countOdd so this time it also checks the elements in a nested list. 
        Write the additional test cases in your unittest file.

        Doctest:
            >>> countOdd([-3,-5,6])
            2
            >>> countOdd([1,2,'Hello',-3.15, 9, "5"])
            3
            >>> countOdd(5)
            'Error'
            >>> countOdd('Hello')
            'Error'

            >>> countOdd([-3,-5,6,"Hello",-3.15, 9, "5",[1,3,5],[9,'3','Hi']])
            9
            >>> countOdd([-3,-5,6])
            2
            >>> countOdd([1,2,"Hello",-3.15, 9, "5"])
            3
            >>> countOdd(5)
            'Error'
            >>> countOdd('Hello')
            'Error'
            >>> countOdd('3.4')
            'Error'
    '''

    def checkList(aList):
        # Check list index types
        for i in range(len(aList)):

            if type(aList[i]) == int:
                
                if aList[i] % 2 != 0:
                    x+=1

            elif type(aList[i]) == str:

                # if the str is numeric check it
                if aList[i].isnumeric():

                    if int(aList[i]) % 2 != 0 and '.' not in aList[i]:
                        x+=1
        
            elif type(aList[i]) == list:

                # Iterate through the list
                x+=checkList(aList[i])                    

    x = 0

    # Input rejection
    if type(aList) != list:
        return 'Error'

    return checkList(aList)

if __name__ == "__main__":
    import doctest
    doctest.testmod()