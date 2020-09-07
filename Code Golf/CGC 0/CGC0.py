
from typing import final


def finalQuizScore(l,h,q1,q2,p):
    '''
        Challenge 0 details:
        ~~~~~~
        - Write a function that finds the minimum integer final quiz score required to get a A- (90%) in this course, given scores for labs, homework, quizzes, and participation.
        - Minimum score must be an integer out of a scale of 100.
        - Type checking is not required. All inputs will be a number between 0 and 100.
        - Function name must be finalQuizScore, and it must take exactly five parameters (lab, homework, quiz 1, quiz 2, participation).
            Example: def finalQuizScore (lab, hw, quiz1, quiz2, part):
        - Return string must be in the format (for example, 65%):
            "You would need a 65% on the final quiz to get an A-."
        - If required score is impossible, return (for example, 120%):
            "Sorry, you would need a 120% on the final quiz to get an A-."

        Doctest:
            >>> finalQuizScore(90, 90, 90, 90, 90)
            'You would need a 90% on the final quiz to get an A-.'
            >>> finalQuizScore(100, 100, 100, 100, 100)
            'You would need a 0% on the final quiz to get an A-.'
            >>> finalQuizScore(80, 80, 80, 80, 80)
            'Sorry, you would need a 180% on the final quiz to get an A-.'
            >>> finalQuizScore(81, 83, 85, 87, 90.5)
            'Sorry, you would need a 150% on the final quiz to get an A-.'
            >>> finalQuizScore(100, 100, 50, 50, 98)
            'Sorry, you would need a 101% on the final quiz to get an A-.'
    '''

    f=int((90-(l*.3)-(h*.35)-(q1*.1)-(q2*.1)-(p*.05))*10)
    if f>100:return 'Sorry, you would need a '+str(f)+'% on the final quiz to get an A-.'
    else:return 'You would need a '+str(f)+'% on the final quiz to get an A-.'
    
if __name__ == "__main__":

    import doctest
    doctest.testmod()