import unittest
from HW2 import *

class Test(unittest.TestCase):
    
    def test_course(self):
        '''
            >>> c2
            CMPSC360(3): Discrete Mathematics
            >>> c3
            CMPSC132(3): Programming in Python II
            >>> c1 == None
            False
            >>> print(c1)
            CMPSC132(3): Programming in Python II
        '''
        ###

        '>>> c1 = Course('CMPSC132', 'Programming in Python II', 3)'
        '>>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)'
        c1 = Course('CMPSC132', 'Programming in Python II', 3)
        c2 = Course('CMPSC360', 'Discrete Mathematics', 3)

        '>>> c1 == c2'
        'False'
        self.assertEqual( c1 == c2, False, 'Course Failed __eq__' )

        '>>> c3 = Course('CMPSC132', 'Programming in Python II', 3)'
        c3 = Course('CMPSC132', 'Programming in Python II', 3)

        '>>> c1 == c3'
        'True'
        self.assertEqual( c1 == c3, True, 'Course Failed __eq__' )

        '>>> c1'
        'CMPSC132(3): Programming in Python II'
        self.assertEqual( str(c1), 'CMPSC132(3): Programming in Python II', 'Course Failed __str__' )

    def test_catalog(self):
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

    def test_semester(self):
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

    def test_loan(self):
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

    def test_person(self):
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
            >>> s
            Student(Jason Smith, js2629, Freshman)
        '''

if __name__ == '__main__':
    
	unittest.main(exit=False)
