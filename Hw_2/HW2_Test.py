import unittest
from HW2 import *

class Test(unittest.TestCase):
    
    def test_course(self):

        '>>> c1 = Course(''CMPSC132'', ''Programming in Python II'', 3)'
        '>>> c2 = Course(''CMPSC360'', ''Discrete Mathematics'', 3)'
        c1 = Course('CMPSC132', 'Programming in Python II', 3)
        c2 = Course('CMPSC360', 'Discrete Mathematics', 3)

        '>>> c1 == c2'
        'False'
        self.assertEqual( c1 == c2, False, 'Course Failed __eq__' )

        '>>> c3 = Course(''CMPSC132'', ''Programming in Python II'', 3)'
        c3 = Course('CMPSC132', 'Programming in Python II', 3)

        '>>> c1 == c3'
        'True'
        self.assertEqual( c1 == c3, True, 'Course Failed __eq__' )

        '>>> c1'
        'CMPSC132(3): Programming in Python II'
        self.assertEqual( str(c1), 'CMPSC132(3): Programming in Python II', 'Course Failed __str__' )

        '>>> c2'
        'CMPSC360(3): Discrete Mathematics'
        self.assertEqual( str(c2), 'CMPSC360(3): Discrete Mathematics', 'Course Failed __str__' )

        '>>> c3'
        'CMPSC132(3): Programming in Python II'
        self.assertEqual( str(c3), 'CMPSC132(3): Programming in Python II', 'Course Failed __str__' )

        '>>> c1 == None'
        'False'
        self.assertEqual( c1 == None, False, 'Course Failed __eq__' )

        '>>> print(c1)'
        'CMPSC132(3): Programming in Python II'
        # ** Tested - Works

    def test_catalog(self):

        '>>> C = Catalog()'
        C = Catalog()

        '>>> C.addCourse(''CMPSC132'', ''Programming in Python II'', 3)'
        'Course added successfully'
        self.assertEqual(C.addCourse('CMPSC132', 'Programming in Python II', 3), 'Course added successfully', 'Failed to add course')

        '>>> C.addCourse(''CMPSC360'', ''Discrete Mathematics'', 3)'
        'Course added successfully'
        self.assertEqual(C.addCourse('CMPSC360', 'Discrete Mathematics', 3), 'Course added successfully', 'Failed to add course')

        # Variable
        d = {'CMPSC132': 'CMPSC132(3): Programming in Python II', 'CMPSC360': 'CMPSC360(3): Discrete Mathematics'}

        '>>> C.courseOfferings'
        '{''CMPSC132'': CMPSC132(3): Programming in Python II, ''CMPSC360'': CMPSC360(3): Discrete Mathematics}'
        self.assertEqual( C.courseOfferings, d, 'Failed to get attr courseOfferings' )

        '>>> C.removeCourse(''CMPSC360'')'
        'Course removed successfully'
        self.assertEqual( C.removeCourse('CMPSC360'), 'Course removed successfully', 'Failed to delete course')

        # Variable
        d = {'CMPSC132': 'CMPSC132(3): Programming in Python II'}

        '>>> C.courseOfferings'
        '{''CMPSC132'': CMPSC132(3): Programming in Python II}'
        self.assertEqual( C.courseOfferings, d, 'Failed to get attr courseOfferings' )

    def test_semester(self):
  
        '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course('MATH 230', 'Calculus', 4)
        >>> phys213 = Course('PHYS 213', 'General Physics', 2)
        >>> econ102 = Course('ECON 102', 'Intro to Economics', 3)
        >>> phil119 = Course('PHIL 119', 'Ethical Leadership', 3)
        '''
        cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        math230 = Course('MATH 230', 'Calculus', 4)
        phys213 = Course('PHYS 213', 'General Physics', 2)
        econ102 = Course('ECON 102', 'Intro to Economics', 3)
        phil119 = Course('PHIL 119', 'Ethical Leadership', 3)
        japns001 = Course('JAPNS 001', 'Japanese I', 4)
        '>>> semester = Semester(1)'
        semester = Semester(1)

        '>>> semester'
        'No courses'
        self.assertEqual( str(semester), 'No courses', 'Failed to distinguish between classes')

        '>>> semester.addCourse(cmpsc132)'
        '>>> semester.addCourse(math230)'
        semester.addCourse(cmpsc132)
        semester.addCourse(math230)
        
        # Variable
        c = 'CMPSC132(3): Programming in Python II, MATH 230(4): Calculus'

        '>>> semester'
        'CMPSC132(3): Programming in Python II, MATH 230(4): Calculus'
        self.assertEqual( str(semester), c, 'Failed to get classes from semester')

        '>>> semester.isFullTime'
        'False'
        self.assertEqual(semester.isFullTime, False, 'Failed to get False fulltime')
  
        '>>> semester.totalCredits'
        '7'
        self.assertEqual(semester.totalCredits, 7, 'Failed to get semesters credits')

        '>>> semester.addCourse(phys213)'
        '>>> semester.addCourse(econ102)'
        semester.addCourse(phys213)
        semester.addCourse(econ102)

        '>>> semester.addCourse(econ102)'
        'Course already added'
        self.assertEqual( semester.addCourse(econ102), 'Course already added', 'Failed to find class already added')

        '>>> semester.addCourse(phil119)'
        semester.addCourse(phil119)

        '>>> semester.isFullTime'
        'True'
        self.assertEqual( semester.isFullTime, True, 'Failed to get True fulltime')

        '>>> semester.dropCourse(phil119)'
        '>>> semester.addCourse(Course(''JAPNS 001'', ''Japanese I'', 4))'
        semester.dropCourse(phil119)
        semester.addCourse(Course('JAPNS 001', 'Japanese I', 4))

        '>>> semester.totalCredits'
        '16'
        self.assertEqual(semester.totalCredits, 16, 'Failed to get total credits')

        '>>> semester.dropCourse(cmpsc131)'
        'No such course'
        self.assertEqual(semester.dropCourse(cmpsc131), 'No such course', 'Failed to find nonexistant course')

        '>>> semester.addCourse(Course(42, name, zero credits))'
        'Invalid course'
        self.assertEqual(semester.addCourse(Course(42, 'name','zero credits')), 'Invalid course', 'Failed to find invalid course')

        # Varaiable
        # c = [CMPSC132(3): Programming in Python II, MATH 230(4): Calculus, PHYS 213(2): General Physics, ECON 102(3): Intro to Economics, JAPNS 001(4): Japanese I]
        c = [cmpsc132, math230, phys213, econ102, japns001]

        '>>> semester.courses'
        '''[CMPSC132(3): Programming in Python II, MATH 230(4): Calculus, PHYS 213(2): General Physics, ECON 102(3): Intro to Economics, JAPNS 001(4): Japanese I]'''
        self.assertEqual(semester.courses, c, 'Failed to get semesters courses')

    def test_loan(self):

        '''
            >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        '''
        s1 = Student('Jason Lee', '204-99-2890', 'Freshman')

        '''
            >>> s1.getLoan(4000)
            'Not full-time'
        '''
        self.assertEqual(s1.getLoan(4000), 'Not full-time', 'Not fulltime for loan')

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
        '''
        C = Catalog()
        self.assertEqual( C.addCourse('CMPSC132', 'Programming in Python II', 3), 'Course added successfully', 'Failed to add course')
        self.assertEqual( C.addCourse('CMPSC360', 'Discrete Mathematics', 3), 'Course added successfully', 'Failed to add course')
        self.assertEqual( C.addCourse('MATH 230', 'Calculus', 4), 'Course added successfully', 'Failed to add course')
        self.assertEqual( C.addCourse('PHYS 213', 'General Physics', 2), 'Course added successfully', 'Failed to add course')

        '''
            >>> s1.registerSemester()
        '''
        s1.registerSemester()

        '''
            >>> s1.enrollCourse('CMPSC132', C,1)
            'Course added successfully'
            >>> s1.enrollCourse('CMPSC360', C,1)
            'Course added successfully'
        '''
        self.assertEqual(s1.enrollCourse('CMPSC132', C,1), 'Course added successfully', 'Failed to add course')
        self.assertEqual(s1.enrollCourse('CMPSC360', C,1), 'Course added successfully', 'Failed to add course')

        '''
            >>> s1.getLoan(4000)
            'Not full-time'
        '''
        self.assertEqual(s1.getLoan(4000), 'Not full-time', 'Not fulltime for loan')

        '''
            >>> s1.enrollCourse('MATH 230', C,1)
            'Course added successfully'
            >>> s1.enrollCourse('PHYS 213', C,1)
            'Course added successfully'
        '''
        self.assertEqual(s1.enrollCourse('MATH 230', C,1), 'Course added successfully', 'Failed to add course')
        self.assertEqual(s1.enrollCourse('PHYS 213', C,1), 'Course added successfully', 'Failed to add course')

        # Variable
        t = {27611: 'Balance: $4000'}

        '''
            >>> s1.getLoan(4000)
            >>> s1.account.loans
            {27611: Balance: $4000}
        '''
        s1.getLoan(4000)
        self.assertEqual(s1.account.loans, t, 'Failed to get loan info' )

        # Variable
        t = {27611: 'Balance: $4000', 84606: 'Balance: $6000'}

        '''
            >>> s1.getLoan(6000)
            >>> s1.account.loans
            {27611: Balance: $4000, 84606: Balance: $6000}
        '''
        s1.getLoan(6000)
        self.assertEqual(s1.account.loans, t, 'Failed to get loan info' )

    def test_person(self):

        '''
            >>> p1 = Person('Jason Lee', '204-99-2890')
            >>> p2 = Person('Karen Lee', '247-01-2670')
            >>> p3 = Person('Karen Smith', '247-01-2670')
        '''
        p1 = Person('Jason Lee', '204-99-2890')
        p2 = Person('Karen Lee', '247-01-2670')
        p3 = Person('Karen Smith', '247-01-2670')

        '''
            >>> p1
            Person(Jason Lee, ***-**-2890)
        '''
        self.assertEqual(str(p1), 'Person(Jason Lee, ***-**-2890)', 'Failed to get p1 __str__')

        '''
            >>> p2
            Person(Karen Lee, ***-**-2670)
        '''
        self.assertEqual(str(p2), 'Person(Karen Lee, ***-**-2670)', 'Failed to get p2 __str__')

        '''
            >>> p3
            Person(Karen Smith, ***-**-2670)
        '''
        self.assertEqual(str(p3), 'Person(Karen Smith, ***-**-2670)', 'Failed to get p3 __str__')

        '''
            >>> p2 == p3
            True
        '''
        self.assertEqual(p2 == p3, True, 'Failed to check SSN')

        '''
            >>> p1 == p2
            False
        '''
        self.assertEqual(p1 == p2, False, 'Failed to check SSN')

    def test_staff(self):
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

    def test_student(self):
        '''

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

        '''
            >>> C = Catalog()
            >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
            'Course added successfully'
            >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
            'Course added successfully'
        '''
        C = Catalog()
        self.assertEqual( C.addCourse('CMPSC132', 'Programming in Python II', 3), 'Course added successfully', 'Failed to add course to catalog' )
        self.assertEqual( C.addCourse('CMPSC360', 'Discrete Mathematics', 3), 'Course added successfully', 'Failed to add course to catalog' )

        '''
            >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
            >>> s1
            Student(Jason Lee, jl2890, Freshman)
            >>> s2 = Student('Karen Lee', '247-01-2670', 'Sophomore')
            >>> s2
            Student(Karen Lee, kl2670, Sophomore)
        '''
        s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        s2 = Student('Karen Lee', '247-01-2670', 'Sophomore')
        
        self.assertEqual( str(s1), 'Student(Jason Lee, jl2890, Freshman)', 'Failed to s1 __str__' )
        self.assertEqual( str(s2), 'Student(Karen Lee, kl2670, Sophomore)', 'Failed to s1 __str__' )

        '''
            >>> s1 == s2
            False
        '''
        self.assertEqual(s1 == s2, False, 'Failed to distinguish students')
    
        '''
            >>> s1.id
            'jl2890'
            >>> s2.id
            'kl2670'
        '''
        self.assertEqual(s1.id, 'jl2890', 'Failed to get ID')
        self.assertEqual(s2.id, 'kl2670', 'Failed to get ID')

        '''
            >>> s1.registerSemester()
            >>> s1.enrollCourse('CMPSC132', C,1)
            'Course added successfully'
        '''
        s1.registerSemester()
        self.assertEqual( s1.enrollCourse('CMPSC132', C, 1), 'Course added successfully')

        

    def test_studentAccount(self):
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

    def test_createStudent(self):

        '''
            >>> p = Person('Jason Smith', '221-11-2629')  
            >>> s = createStudent(p)  
        '''
        p = Person('Jason Smith', '221-11-2629')
        s = createStudent(p)  

        '''
            >>> s
            Student(Jason Smith, js2629, Freshman)
        '''
        self.assertEqual(str(s), 'Student(Jason Smith, js2629, Freshman)', 'Failed to get __str__')

if __name__ == '__main__':
    
	unittest.main(exit=False)
