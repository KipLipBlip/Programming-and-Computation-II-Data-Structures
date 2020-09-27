# HW2
#Due Date: 09/25/2020, 11:59PM
'''                                   
### Collaboration Statement:
    I worked on this assignment alone, using only this semester's course materials
'''

import random

# ! DONE
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
        if isinstance(other, Course):
            # Compare IDs
            if self.cid == other.cid:
                return True
            else:
                return False
        else:
            return False

# ! DONE
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
            self.courseOfferings[cid] = Course(cid, cname, credits)
            return 'Course added successfully'

        else:
            return 'Course already added' 

    def removeCourse(self, cid):

        # Check if the course is already in the dict
        if cid in self.courseOfferings:
            
            del self.courseOfferings[cid]
            return 'Course removed successfully'

        else:
            return 'Course not found'

# ! DONE
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
        self.courses = ['No courses']

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

            # Check types b/c not asked to initially check in course class
            if isinstance(course.cid, str) and isinstance(course.cname, str) and isinstance(course.credits, int):

                # Check if the course is already under this semesters courses
                if course not in self.courses:

                    # Remove the 'No courses'
                    if self.courses[0] == 'No courses':
                        self.courses.pop(0)

                    self.courses.append(course)
                else:
                    return 'Course already added'
            else:
                return 'Invalid course'
        else:
            return 'Invalid course'        

    def dropCourse(self, course):

        # Check the object
        if isinstance(course, Course):

            # Check if course is in this semester
            if course in self.courses:
                
                self.courses.remove(course)

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
        if self.totalCredits >= 12:
            return True
        else: 
            return False

# COme back after student 
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
        self.amount = amount
        self.loan_id = self.__loanID

    def __str__(self):
        return '${}'.format(self.amount)

    __repr__ = __str__

    @property
    def __loanID(self):
        return random.randint(10000, 99999)

# ! DONE
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

        # Set name and set private ssn
        self.name = name
        self.__ssn = ssn

    def __str__(self):
        # Put the last four digits in a string and format
        t = self.get_ssn()
        return 'Person({}, ***-**-{})'.format(self.name, t[-4]+t[-3]+t[-2]+t[-1])

    __repr__ = __str__

    def get_ssn(self):
        return self.__ssn

    def __eq__(self, other):

        # Check if other is a person object
        if isinstance(other, Person):

            # Check if the ssn's are the same via getter
            if other.get_ssn() == self.get_ssn():
                return True
            else:
                return False
        else:
            return False

# ! DONE
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

        self.name = name
        self.ssn = ssn
        self.__supervisor = supervisor

    def __str__(self):
        return f'Staff({self.name}, {self.id})'

    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, Staff):
            if self.ssn == other.ssn:
                return True
            else:
                return False
        else:
            return False

    @property
    def id(self):
        # Returning the staff ID, 905+initials+last four of ssn
        lastFour = self.ssn[-4] + self.ssn[-3] + self.ssn[-2] + self.ssn[-1]
        initials = self.name.split()
        initials = initials[0][0].lower() + initials[1][0].lower()
        return f'905{initials}{lastFour}'

    @property   
    def getSupervisor(self):
        return self.__supervisor

    def setSupervisor(self, new_supervisor):
        if isinstance(new_supervisor, Staff):
            self.__supervisor = new_supervisor
            return 'Completed!'
        else:
            return None

    def applyHold(self, student):
        if isinstance( student, Student):
            student.hold = True
            return 'Completed!'
        else:
            return None

    def removeHold(self, student):
        if isinstance( student, Student):
            student.hold = False
            return 'Completed!'
        else:
            return None

    def unenrollStudent(self, student):
        if isinstance( student, Student):
            student.active = False
            return 'Completed!'
        else:
            return None

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

        self.year = year            # A string indicating the student’s year ("Freshman", etc.). 
        self.name = name
        self.ssn = ssn
        self.semesters = {}         # A collection of Semester objects accessible by sem_num.
        self.hold = False           # Indicates a hold on the student’s account, defaults to False.
        self.active = True          # Indicates if the student is actively enrolled, defaults to True.

        self.account = self.__createStudentAccount()     # The current balance of the student

    def __str__(self):
        
        return 'Student({}, {}, {})'.format(self.name, self.id, self.year)

    __repr__ = __str__

    def __eq__(self, other):
        # Check object
        if isinstance(other, Student):
            # They will be the same person if they have the same ssn
            if other.ssn == self.ssn:
                return True
            else:
                return False
        else:
            return False

    def __createStudentAccount(self):
        self.account = StudentAccount(self)

    @property
    def id(self):
        ''' 
            Property method (behaves like an attribute) for 
            generating student’s id.The format should be: initials+last 
            four numbers of ssn(e.g.: abc6789). Ignore the security
            flaws this generation method presents and assume ids are unique.
        '''
        # Get the lowercase initials and add the last four of the ssn
        i = self.name.split()
        t = self.ssn
        return i[0][0].lower() + i[1][0].lower() + t[-4]+t[-3]+t[-2]+t[-1]

    def registerSemester(self):
        # Check if applicable
        if self.active and not self.hold:

            # Find the largest semester number and add 1
            n = 0
            for item in self.semesters:
                if item > n:
                    n = item
            
            # Create a semester object and add it to semesters
            self.semesters[n+1] = Semester(n+1)

        else:
            return 'Unsuccessful operation'

    def courseInSemester(self, cid, semester):
        # Find if the cid is in the semester

        for i in range( len( self.semesters[semester].courses )):
            if self.semesters[semester].courses[i].cid == cid:
                return i

    def enrollCourse(self, cid, catalog, semester):
        # Check if applicable
        if not self.hold and self.active:

            # Check for course in catalog
            if cid in catalog.courseOfferings:

                # Check if course in semester already
                if catalog.courseOfferings[cid] not in self.semesters[semester].courses:

                    # Check if there is 'No courses' in the semesters list
                    if self.semesters[semester].courses[0] == 'No courses':
                        self.semesters[semester].courses.pop(0)

                    # Add the course to the semester
                    self.semesters[semester].courses.append( catalog.courseOfferings[cid] ) 
                    return 'Course added successfully'
                    
                else:
                    return 'Course already enrolled'
                
            else:
                return 'Course not found'

        else:
            return 'Unsuccessful operation'

    def dropCourse(self, cid, semester):
        # Check if applicable
        if not self.hold and self.active:

            # Check for course in semester
            if self.courseInSemester(cid, semester):
                
                # Remove the course
                del self.semesters[semester].courses[ self.courseInSemester(cid, semester) ]
                return 'Course dropped successfully'

            else:
                return 'Course not found'

        else:
            return 'Unsuccessful operation'

    def getLoan(self, amount):
        # Check if applicable
        if not self.hold:

            if self.active:

                # If self.semesters is empty the student cannot be fulltime
                if len(self.semesters.keys()) != 0:

                    # Get the current semester
                    t = len(self.semesters.keys())
                    if t > 1:
                        t -= 1
                    
                    if self.semesters[ t ].isFullTime:
                        
                    # Get the loan object and add it to the student's account, add the loan balance to the students account
                        temp = Loan(amount)

                    else:
                        return 'Not full-time'
                else:
                    return 'Not full-time'
            else:
                return 'Not full-time'
        else:
            return 'Unsuccessful operation'

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
    creditPrice = 1000

    def __init__(self, student):
        self.student = student
        self.balance = 0
        self.loans = {}

    def __str__(self):
        # YOUR CODE STARTS HERE
        pass

    __repr__ = __str__

    def makePayment(self, amount, loan_id=None):
        # No loan ID
        if loan_id == None:
            self.balance -= amount
            return f'${self.balance}'
        
        # Loan ID
        else:
            # Check for loan in self.loans
            if loan_id in self.loans:

                # Paying more then the value of the loan?
                if amount >= self.loans[loan_id]:
                    self.loans[loan_id] -= self.loans[loan_id]
                    self.balance -= (amount - self.loans[loan_id])
                    return f'Loan Balance: {self.loans[loan_id]}'

                else:
                    self.loans[loan_id] -= amount
                    return 

            else:
                return None

    def chargeAccount(self, amount):
        self.balance += amount
        return f'${self.balance}'

# Outside of classes

# ! DONE
def createStudent(person):
    '''
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> s = createStudent(p)
        >>> s
        Student(Jason Smith, js2629, Freshman)
    '''
    return Student(person.name, person.get_ssn(), 'Freshman')