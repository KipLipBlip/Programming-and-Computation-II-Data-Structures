# HW3
# Due Date: 10/24/2020, 11:59PM
"""                                   
### Collaboration Statement: 
    I worked on this assignment alone using only this semester's course materials             
"""



from typing import Text


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

# ** DONE

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''

    def __init__(self):
        self.top=None
        self.count=0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        return self.top == None

    def __len__(self):
        return self.count

    def push(self,e):
        # Add a new node to the top of the stack
        newNode = Node(e)           # Create node
        newNode.next = self.top     # Create link
        self.top = newNode          # New top
        self.count += 1             # Increment count size

    def pop(self):
        # Pop the top node, return the top node's value, not object
        if self.isEmpty():          # Validation
            return None
        temp = self.top.value       # Temporarily store value to be returned
        self.top = self.top.next    # Reassign top
        self.count -= 1             # Decrement count size
        return temp                 # Return temp value

    def peek(self):
        # Return the VALUE of the top node, not the object
        if self.isEmpty():      # Validation
            return None
        return self.top.value   # Return the VALUE of the top node

#=============================================== Part II ==============================================

class Calculator:

    # Infix: 4 + 3 - 2 * 4
    # Postfix: 4 3 2 4 * - +

    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def isNumber(self, txt):
        # Returns True if txt can be converted to a float
        try:
            float(txt)
            return True
        except ValueError:
            return False

    def validation(self, txt):
        '''
            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary        
            
            >>> x = Calculator()
            >>> x.validation('2 * 5 + 3 ^ + -2 + 1 + 4')
            [ERROR]: Two consecutive operators, no operand [^, +]
            >>> x.validation('2 * 5 + 3 ^ - 2 + 1 + 4')
            [ERROR]: Two consecutive operators, no operand [^, -]
            >>> x.validation('2    5')
            [ERROR]: Two consecutive operands, no operator [2, 5]
            >>> x.validation('25 +')
            [ERROR]: Expression ends with operator [+]
            >>> x.validation(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            [ERROR]: Mismatching parenthesis in expression
            >>> x.validation(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            [ERROR]: Incorrect parenthesis alignment
            >>> x.validation('2 * 5% + 3 ^ + -2 + 1 + 4')
            [ERROR]: Two consecutive operators, no operand [*, 5%]
        '''

        operators = ['^', '(', ')', '+', '-', '*', '/']

        if isinstance(txt, str):
        
            if '(' in txt or ')' in txt:
                
                # Match parenthesis

                if txt.count('(') == txt.count(')'):
                    
                    for q in range(txt.count('(')):

                        L = txt.index('(')
                        R = txt.index(')')

                        if L > R:
                            print('[ERROR]: Incorrect parenthesis alignment')
                            return None

                        txt = txt[:L] + txt[L+1:]   # Reconstruct
                        txt = txt[:R-1] + txt[R:]   # Reconstruct

                else:

                    print('[ERROR]: Mismatching parenthesis in expression')
                    return None

            txt = txt.split()

            if len(txt) <= 0:
                
                print('[ERROR]: Empty expression')
                return None

            for i in range(len(txt)):

                if not self.isNumber(txt[i]) and txt[i] not in operators:

                    # Unsupported operators

                    if txt[i] == '**':
                        print(f'[ERROR]: Use ^ for exponentiation')
                        return None

                    else:
                        print(f'[ERROR]: Unsupported operator [{txt[i]}]')
                        return None

                else:

                    # Find missing operator

                    if not len(txt) == i+1:

                        if self.isNumber(txt[i]) and self.isNumber(txt[i+1]):

                            # Two numbers next to eachother

                            print(f'[ERROR]: Two consecutive operands, no operator [{txt[i]}, {txt[i+1]}]')
                            return None

                        elif not self.isNumber(txt[i]) and not self.isNumber(txt[i+1]):

                            # Two operators next to eachother

                            if not (( txt[i] in operators and txt[i+1] == '(' ) or ( txt[i] == ')' and txt[i+1] in operators )):

                                # Incorrect implicit operators

                                print(f'[ERROR]: Two consecutive operators, no operand [{txt[i]}, {txt[i+1]}]')
                                return None

            if txt[0] in operators and txt[0] != '(':

                # Starts with operator

                print(f'[ERROR]: Expression starts with operator [{txt[0]}]')
                return None

            elif txt[-1] in operators and txt[-1] != ')':

                # Ends with operator

                print(f'[ERROR]: Expression ends with operator [{txt[-1]}]')
                return None

        else:
            print('[Error]: Expression must be entered as a string')
            return None

        return True

    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary
        '''

        precedence = { '-': 1, '+': 1, '/': 3, '*': 2, '^': 4, '(': 0, ')': 0}
        PF = ''

        postOp = Stack()
        
        txt = txt.split()   

        for i in range(len(txt)):      

            if txt[i] == ')':
                
                while postOp.top.value != '(':

                    PF += postOp.pop() + ' '

                    if postOp.isEmpty() or postOp.top == None:
                        break

                else:

                    postOp.pop()


            elif not postOp.isEmpty() and i+1 == len(txt):

                # Add the last index

                if txt[i] not in precedence:
                    
                    PF += str(float(txt[i])) + ' '

                else:

                    postOp.push(txt[i])

                # Empty the stack

                while not postOp.isEmpty():
                                        
                    PF += postOp.pop() + ' '

            elif txt[i] in precedence:

                if txt[i] == '(':
                    
                    postOp.push(txt[i])

                elif postOp.isEmpty():

                    postOp.push(txt[i])

                # Check for precendence
                else:

                    if precedence[txt[i]] < precedence[postOp.top.value]:

                        # Pop until we find lower precedence then txt[i]

                        while precedence[txt[i]] <= precedence[postOp.top.value]:

                            if postOp.top.value == '(':
                                postOp.pop()

                            else:
                                PF += postOp.pop() + ' '

                            if postOp.isEmpty():
                                break

                        postOp.push(txt[i])

                    elif precedence[txt[i]] > precedence[postOp.top.value]:
                        
                        postOp.push(txt[i])

                    elif precedence[txt[i]] == precedence[postOp.top.value]:

                        PF += postOp.pop() + ' '
                        postOp.push(txt[i])


            elif self.isNumber(txt[i]):

                # Add to return string
                PF += str(float(txt[i])) + ' '

            # Invalid cases
            else:

                if not txt[i].isnumeric() and txt[i] not in precedence:
                    print('[ERROR]: Invalid operator')
                    return None


        # Make sure stack is empty before return

        if not postOp.isEmpty():

            # Empty the stack

            while not postOp.isEmpty():
                PF += postOp.pop() + ' '

        # Remove the addistional space at the end
        return PF[:len(PF)-1]

    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr(' 3 * ( ( ( 10 - 2 * 3 ) ) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2")
            >>> x.calculate
            [ERROR]: Two consecutive operators, no operand [+, +]
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            [ERROR]: Two consecutive operands, no operator [4, 3]
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            [ERROR]: Mismatching parenthesis in expression
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            [ERROR]: Two consecutive operators, no operand [*, /]
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            [ERROR]: Incorrect parenthesis alignment
        '''

        if not isinstance(self.__expr, str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calculateStack=Stack()

        if self.validation(self.getExpr):

            PF = self._getPostfix(self.__expr)

            PF = PF.split()

            for i in range(len(PF)):

                if self.isNumber(PF[i]):

                    # This is an operand
                    calculateStack.push(PF[i])

                else:

                    # This is an operator
                    n1 = float(calculateStack.pop())
                    n2 = float(calculateStack.pop())

                    if PF[i] == '+':
                        calculateStack.push(n1 + n2)

                    elif PF[i] == '-':
                        calculateStack.push(n2 - n1)

                    elif PF[i] == '/':
                        calculateStack.push(n2 / n1)

                    elif PF[i] == '^':
                        calculateStack.push(n2 ** n1)

                    elif PF[i] == '*':
                        calculateStack.push(n1 * n2)

            return calculateStack.top.value

        else:
            return None


# #=============================================== Part III ==============================================

# class AdvancedCalculator:
#     '''
#     >>> C = AdvancedCalculator()
#     >>> C.states == {}
#     True
#     >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
#     >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
#     True
#     >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
#     True
#     >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2')
#     >>> C.states == {}
#     True
#     >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 28.0}
#     True
#     >>> print(C.calculateExpressions())
#     {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 28.0}
#     >>> C.states == {'x1': 23.0, 'x2': 28.0}
#     True
#     >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1')
#     >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 24.5}
#     True
#     >>> C.states == {'x1': 24.5, 'x2': 427.0}
#     True
#     >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D')
#     >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 41.0}
#     True
#     >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
#     True
#     '''
#     def __init__(self):
#         self.expressions = ''
#         self.states = {}

#     def setExpression(self, expression):
#         self.expressions = expression
#         self.states = {}

#     def isVariable(self, word):
#         '''
#             >>> C = AdvancedCalculator()
#             >>> C.isVariable('volume')
#             True
#             >>> C.isVariable('4volume')
#             False
#             >>> C.isVariable('volume2')
#             True
#             >>> C.isVariable('vol%2')
#             False
#         '''
#         # YOUR CODE STARTS HERE
#         pass
       

#     def replaceVariables(self, expr):
#         '''
#             >>> C = AdvancedCalculator()
#             >>> C.states = {'x1': 23.0, 'x2': 28.0}
#             >>> C.replaceVariables('1')
#             '1'
#             >>> C.replaceVariables('7 * ( x1 - 1 )')
#             '7 * ( 23.0 - 1 )'
#             >>> C.replaceVariables('x2 - x1')
#             '28.0 - 23.0'
#         '''

#         # YOUR CODE STARTS HERE
#         pass

    
#     def calculateExpressions(self):
#         self.states = {} 
#         calc = Calculator()
#         # YOUR CODE STARTS HERE
#         pass