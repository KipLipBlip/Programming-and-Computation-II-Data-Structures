# HW2
#Due Date: 09/25/2020, 11:59PM
'''                                   
### Collaboration Statement:
    I worked on this assignment alone, using only this semester's course materials
'''

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''

    def __init__(self, cid, cname, credits):
        ''' Set initial class attributes. '''

        self.cid = cid
        self.cname = cname
        self.credits = credits
        
    def __str__(self):
        ''' Returns a formatted summary of the course as a string. '''

        # ID(credits): Name
        return '{}({}): {}'.format(self.cid, self.credits, self.cname)

    __repr__ = __str__

    def __eq__(self, other):
        ''' Does an equality check based only on course id ''' 
        
        # Compare IDs
        try:
            if self.cid == other.cid:
                return True
            else:
                return False
        except AttributeError:
            return False

class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'CMPSC360': CMPSC360(3): Discrete Mathematics}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II}
    '''
    def __init__(self):
        ''' Initialize the dictionary catalog '''
        
        # 'ID' : 'ID(credits): Name'
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits):
        ''' Creates a course with the parameters and stores that course in courseOfferings. '''
        
        # Check if the course is already in the dict
        if cid not in self.courseOfferings:
            # Add the course --> 'ID' : 'ID(credits): Name'
            self.courseOfferings[cid] = '{}({}): {}'.format(cid, credits, cname)
            return 'Course added successfully'
        else:
            return 'Course already added' 

    def removeCourse(self, cid):
        ''' Removes a course with the given id. '''

        # Check if the course is already in the dict
        if cid in self.courseOfferings:
            # Add the course --> 'ID' : 'ID(credits): Name'
            del self.courseOfferings[cid]
            return 'Course removed successfully'
        else:
            return 'Course not found'

class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course('MATH 230', 'Calculus', 4)
        >>> phys213 = Course('PHYS 213', 'General Physics', 2)
        >>> econ102 = Course('ECON 102', 'Intro to Economics', 3)
        >>> phil119 = Course('PHIL 119', 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132(3): Programming in Python II, MATH 230(4): Calculus
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course('JAPNS 001', 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.addCourse(Course(42, 'name','zero credits'))
        'Invalid course'
        >>> semester.courses
        [CMPSC132(3): Programming in Python II, MATH 230(4): Calculus, PHYS 213(2): General Physics, ECON 102(3): Intro to Economics, JAPNS 001(4): Japanese I]
    '''

    def __init__(self, sem_num):
        
        self.sem_num = sem_num
        self.courses = []

    def __str__(self):
        ''' Return the formatted string of the semester's courses. '''

        # If there are courses, return then as a joined str
        if len(self.courses) > 0:
            return ''.join(str(self.courses))
        else:
            return 'No courses'

    __repr__ = __str__

    def addCourse(self, course):
        ''' Adds a course to courses if it is a valid course object. '''

        # Check the attributes
        if isinstance(course, Course):

            # Check if the course is already under this semesters courses
            if course not in self.courses:
                # Add the course [ {cid : [cname, credits]}, ... ]
                self.courses.append(course)
            else:
                return 'Course already added'
        else:
            return 'Invalid course'        

    def dropCourse(self, course):
        ''' Removes a course from courses. '''

        # Check the object
        if isinstance(course, Course):

            # Check if course is in this semester
            if course in self.courses:
                
                # Find the index the class is at and pop is
                for i in range(len(self.courses)):
                    if self.courses[i] == course.cid:
                        break
                    self.courses.pop(i)

            else:
                return 'No such course'
        else:
            return 'Invalid course'

    @property
    def totalCredits(self):
        ''' A property method for the total number of credits. '''
        c = 0
        for item in self.courses:
            c += item.credits
        return c

    @property
    def isFullTime(self):
        ''' A property method that returns True if this is full-time. '''
        
        # Check if there are 12 or more credits
        if totalCredits >= 12:
            return True
        else: 
            return False


    
class Loan:
    '''
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC360', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        >>> s1.account.loans
        {27611: Balance: $4000}
        >>> s1.getLoan(6000)
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $6000}
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        pass


    def __str__(self):
        # YOUR CODE STARTS HERE
        pass

    __repr__ = __str__


    @property
    def __loanID(self):
        # YOUR CODE STARTS HERE
        pass


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        pass

    def __str__(self):
        # YOUR CODE STARTS HERE
        pass

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        pass

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        pass

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> st1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: [CMPSC132(3): Programming in Python II]}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: [CMPSC132(3): Programming in Python II]}
    '''
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        pass


    def __str__(self):
        # YOUR CODE STARTS HERE
        pass

    __repr__ = __str__


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        pass

    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        pass

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        pass


    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        pass

    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        pass

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        pass




class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Sophomore')
        >>> s2
        Student(Karen Lee, kl2670, Sophomore)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: [CMPSC132(3): Programming in Python II]}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: [CMPSC132(3): Programming in Python II, CMPSC360(3): Discrete Mathematics]}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course not found'
        >>> s1.semesters
        {1: [CMPSC132(3): Programming in Python II]}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: [CMPSC132(3): Programming in Python II], 2: [No courses]}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: [CMPSC132(3): Programming in Python II], 2: [CMPSC360(3): Discrete Mathematics]}
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE


    def __str__(self):
        # YOUR CODE STARTS HERE
        pass

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        pass


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        pass

    def registerSemester(self):
        # YOUR CODE STARTS HERE
        pass



    def enrollCourse(self, cid, catalog, semester):
        # YOUR CODE STARTS HERE
        pass

    def dropCourse(self, cid, semester):
        # YOUR CODE STARTS HERE
        pass

    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        pass




class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.makePayment(5000, 27611)
        'Loan Balance: 4000'
        >>> s1.account.makePayment(3000, 27611)
        8900
        >>> s1.account.loans
        {27611: Balance: $1000}
    '''
    
    def __init__(self, student):
        # YOUR CODE STARTS HERE
        pass


    def __str__(self):
        # YOUR CODE STARTS HERE
        pass

    __repr__ = __str__


    def makePayment(self, amount, loan_id=None):
        # YOUR CODE STARTS HERE
        pass


    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        pass




######################################################################


def createStudent(person):
    '''
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> s = createStudent(p)
        >>> s
        Student(Jason Smith, js2629, Freshman)
    '''
    pass
