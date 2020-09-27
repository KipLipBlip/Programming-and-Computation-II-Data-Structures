import unittest
from HW2 import *

class Test(unittest.TestCase):

    # ! DONE    
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

    # ! DONE
    def test_catalog(self):

        C = Catalog()

        self.assertEqual(C.addCourse('CMPSC132', 'Programming in Python II', 3), 'Course added successfully', 'Failed to add course')

        self.assertEqual(C.addCourse('CMPSC360', 'Discrete Mathematics', 3), 'Course added successfully', 'Failed to add course')

        # Variable
        d = {'CMPSC132': Course('CMPSC132', 'Programming in Python II', 3), 'CMPSC360': Course('CMPSC360', 'Discrete Mathematics', 3)}

        # self.assertEqual( C.courseOfferings, d, 'Failed to get attr courseOfferings' )

        self.assertEqual( C.removeCourse('CMPSC360'), 'Course removed successfully', 'Failed to delete course')

        # Variable
        d = {'CMPSC132': str(Course('CMPSC132', 'Programming in Python II', 3))}

        # self.assertEqual( C.courseOfferings, d, 'Failed to get attr courseOfferings' )

    # ! DONE
    def test_semester(self):
  
        cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        math230 = Course('MATH 230', 'Calculus', 4)
        phys213 = Course('PHYS 213', 'General Physics', 2)
        econ102 = Course('ECON 102', 'Intro to Economics', 3)
        phil119 = Course('PHIL 119', 'Ethical Leadership', 3)
        japns001 = Course('JAPNS 001', 'Japanese I', 4)
        semester = Semester(1)

        # self.assertEqual( semester, 'No courses', 'Failed to distinguish between classes')

        semester.addCourse(cmpsc132)
        semester.addCourse(math230)
        
        # Variable
        c = 'CMPSC132(3): Programming in Python II, MATH 230(4): Calculus'

        self.assertEqual( str(semester), c, 'Failed to get classes from semester')

        self.assertEqual(semester.isFullTime, False, 'Failed to get False fulltime')

        self.assertEqual(semester.totalCredits, 7, 'Failed to get semesters credits')

        semester.addCourse(phys213)
        semester.addCourse(econ102)

        self.assertEqual( semester.addCourse(econ102), 'Course already added', 'Failed to find class already added')

        '>>> semester.addCourse(phil119)'
        semester.addCourse(phil119)

        self.assertEqual( semester.isFullTime, True, 'Failed to get True fulltime')

        semester.dropCourse(phil119)
        semester.addCourse(Course('JAPNS 001', 'Japanese I', 4))

        self.assertEqual(semester.totalCredits, 16, 'Failed to get total credits')

        self.assertEqual(semester.dropCourse(cmpsc131), 'No such course', 'Failed to find nonexistant course')

        self.assertEqual(semester.addCourse(Course(42, 'name','zero credits')), 'Invalid course', 'Failed to find invalid course')

        # Varaiable
        c = [cmpsc132, math230, phys213, econ102, japns001]

        self.assertEqual(semester.courses, c, 'Failed to get semesters courses')

    # def test_loan(self):

    #     '''
    #         >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
    #     '''
    #     s1 = Student('Jason Lee', '204-99-2890', 'Freshman')

    #     '''
    #         >>> s1.getLoan(4000)
    #         'Not full-time'
    #     '''
    #     self.assertEqual(s1.getLoan(4000), 'Not full-time', 'Not fulltime for loan')

    #     '''
    #         >>> C = Catalog()
    #         >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
    #         'Course added successfully'
    #         >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
    #         'Course added successfully'
    #         >>> C.addCourse('MATH 230', 'Calculus', 4)
    #         'Course added successfully'
    #         >>> C.addCourse('PHYS 213', 'General Physics', 2)
    #         'Course added successfully'
    #     '''
    #     C = Catalog()
    #     self.assertEqual( C.addCourse('CMPSC132', 'Programming in Python II', 3), 'Course added successfully', 'Failed to add course')
    #     self.assertEqual( C.addCourse('CMPSC360', 'Discrete Mathematics', 3), 'Course added successfully', 'Failed to add course')
    #     self.assertEqual( C.addCourse('MATH 230', 'Calculus', 4), 'Course added successfully', 'Failed to add course')
    #     self.assertEqual( C.addCourse('PHYS 213', 'General Physics', 2), 'Course added successfully', 'Failed to add course')

    #     '''
    #         >>> s1.registerSemester()
    #     '''
    #     s1.registerSemester()

    #     '''
    #         >>> s1.enrollCourse('CMPSC132', C,1)
    #         'Course added successfully'
    #         >>> s1.enrollCourse('CMPSC360', C,1)
    #         'Course added successfully'
    #     '''
    #     self.assertEqual(s1.enrollCourse('CMPSC132', C,1), 'Course added successfully', 'Failed to add course')
    #     self.assertEqual(s1.enrollCourse('CMPSC360', C,1), 'Course added successfully', 'Failed to add course')

    #     '''
    #         >>> s1.getLoan(4000)
    #         'Not full-time'
    #     '''
    #     self.assertEqual(s1.getLoan(4000), 'Not full-time', 'Not fulltime for loan')

    #     '''
    #         >>> s1.enrollCourse('MATH 230', C,1)
    #         'Course added successfully'
    #         >>> s1.enrollCourse('PHYS 213', C,1)
    #         'Course added successfully'
    #     '''
    #     self.assertEqual(s1.enrollCourse('MATH 230', C,1), 'Course added successfully', 'Failed to add course')
    #     self.assertEqual(s1.enrollCourse('PHYS 213', C,1), 'Course added successfully', 'Failed to add course')

    #     # Variable
    #     t = {27611: 'Balance: $4000'}

    #     '''
    #         >>> s1.getLoan(4000)
    #         >>> s1.account.loans
    #         {27611: Balance: $4000}
    #     '''
    #     s1.getLoan(4000)
    #     self.assertEqual(s1.account.loans, t, 'Failed to get loan info' )

    #     # Variable
    #     t = {27611: 'Balance: $4000', 84606: 'Balance: $6000'}

    #     '''
    #         >>> s1.getLoan(6000)
    #         >>> s1.account.loans
    #         {27611: Balance: $4000, 84606: Balance: $6000}
    #     '''
    #     s1.getLoan(6000)
    #     self.assertEqual(s1.account.loans, t, 'Failed to get loan info' )

    # ! DONE
    def test_person(self):

        p1 = Person('Jason Lee', '204-99-2890')
        p2 = Person('Karen Lee', '247-01-2670')
        p3 = Person('Karen Smith', '247-01-2670')

        self.assertEqual(str(p1), 'Person(Jason Lee, ***-**-2890)', 'Failed to get p1 __str__')

        self.assertEqual(str(p2), 'Person(Karen Lee, ***-**-2670)', 'Failed to get p2 __str__')

        self.assertEqual(str(p3), 'Person(Karen Smith, ***-**-2670)', 'Failed to get p3 __str__')

        self.assertEqual(p2 == p3, True, 'Failed to check SSN')

        self.assertEqual(p1 == p2, False, 'Failed to check SSN')

    # ! DONE
    def test_staff(self):

            C = Catalog()

            self.assertEqual( C.addCourse('CMPSC132', 'Programming in Python II', 3), 'Course added successfully' )

            self.assertEqual( C.addCourse('CMPSC360', 'Discrete Mathematics', 3), 'Course added successfully' )

            s1 = Staff('Jane Doe', '214-49-2890')
            
            self.assertEqual( s1.getSupervisor, None )

            s2 = Staff('John Doe', '614-49-6590', s1)

            self.assertEqual( str(s2.getSupervisor), 'Staff(Jane Doe, 905jd2890)' )
            
            self.assertEqual( s1 == s2, False)
   
            self.assertEqual( s2.id, '905jd6590')
            
            st1 = Student('Jason Lee', '204-99-2890', 'Freshman')
            
            self.assertEqual( s2.applyHold(st1), 'Completed!')

            self.assertEqual( st1.registerSemester(), 'Unsuccessful operation')
            
            self.assertEqual( s2.removeHold(st1), 'Completed!')

            st1.registerSemester()

            self.assertEqual( st1.enrollCourse('CMPSC132', C, 1), 'Course added successfully')
            
            # self.assertEqual( st1.semesters, {1: ['CMPSC132(3): Programming in Python II']})
            
            self.assertEqual( s1.applyHold(st1), 'Completed!')

            self.assertEqual( st1.enrollCourse('CMPSC360', C, 1), 'Unsuccessful operation')

            # self.assertEqual( st1.semesters, {1: ['CMPSC132(3): Programming in Python II']})

    # def test_student(self):

    #     '''
    #         >>> C = Catalog()
    #         >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
    #         'Course added successfully'
    #         >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
    #         'Course added successfully'
    #     '''
    #     C = Catalog()
    #     self.assertEqual( C.addCourse('CMPSC132', 'Programming in Python II', 3), 'Course added successfully', 'Failed to add course to catalog' )
    #     self.assertEqual( C.addCourse('CMPSC360', 'Discrete Mathematics', 3), 'Course added successfully', 'Failed to add course to catalog' )

    #     '''
    #         >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
    #         >>> s1
    #         Student(Jason Lee, jl2890, Freshman)
    #         >>> s2 = Student('Karen Lee', '247-01-2670', 'Sophomore')
    #         >>> s2
    #         Student(Karen Lee, kl2670, Sophomore)
    #     '''
    #     s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
    #     s2 = Student('Karen Lee', '247-01-2670', 'Sophomore')
        
    #     self.assertEqual( str(s1), 'Student(Jason Lee, jl2890, Freshman)', 'Failed to s1 __str__' )
    #     self.assertEqual( str(s2), 'Student(Karen Lee, kl2670, Sophomore)', 'Failed to s1 __str__' )

    #     '''
    #         >>> s1 == s2
    #         False
    #     '''
    #     self.assertEqual(s1 == s2, False, 'Failed to distinguish students')
    
    #     '''
    #         >>> s1.id
    #         'jl2890'
    #         >>> s2.id
    #         'kl2670'
    #     '''
    #     self.assertEqual(s1.id, 'jl2890', 'Failed to get ID')
    #     self.assertEqual(s2.id, 'kl2670', 'Failed to get ID')

    #     '''
    #         >>> s1.registerSemester()
    #         >>> s1.enrollCourse('CMPSC132', C,1)
    #         'Course added successfully'
    #     '''
    #     s1.registerSemester()
    #     self.assertEqual( s1.enrollCourse('CMPSC132', C, 1), 'Course added successfully')

    #     # Variable
    #     s = {1: ['CMPSC132(3): Programming in Python II']}

    #     '''
    #         >>> s1.semesters
    #         {1: [CMPSC132(3): Programming in Python II]}
    #     '''
    #     self.assertEqual( s1.semesters, s, 'Failed to get semesters')

    #     '''
    #         >>> s1.enrollCourse('CMPSC360', C, 1)
    #         'Course added successfully'
    #     '''
    #     self.assertEqual(s1.enrollCourse('CMPSC360', C, 1), 'Course added successfully', 'Failed to enroll')
        
    #     '''
    #         >>> s1.enrollCourse('CMPSC311', C, 1)
    #         'Course not found'
    #     '''
    #     self.assertEqual(s1.enrollCourse('CMPSC311', C, 1), 'Course not found', 'Failed to find nonexistant course')

    #     # Variable
    #     s = {1: ['CMPSC132(3): Programming in Python II', 'CMPSC360(3): Discrete Mathematics']}

    #     '''
    #         >>> s1.semesters
    #         {1: [CMPSC132(3): Programming in Python II, CMPSC360(3): Discrete Mathematics]}
    #     '''
    #     self.assertEqual( s1.semesters, s, 'Failed to get semesters')

    #     '''
    #         >>> s2.semesters
    #         {}
    #     '''
    #     self.assertEqual( s2.semesters, {}, 'Failed to get semesters')

    #     '''
    #         >>> s1.enrollCourse('CMPSC132', C, 1)
    #         'Course already enrolled'
    #     '''
    #     self.assertEqual(s1.enrollCourse('CMPSC132', C, 1), 'Course already enrolled', 'Failed to find double enrolled course')

    #     '''
    #         >>> s1.dropCourse('CMPSC360', 1)
    #         'Course dropped successfully'
    #     '''
    #     self.assertEqual(s1.dropCourse('CMPSC360', 1), 'Course dropped successfully', 'Failed drop course')

    #     '''
    #         >>> s1.dropCourse('CMPSC360', 1)
    #         'Course not found'
    #     '''
    #     self.assertEqual(s1.dropCourse('CMPSC360', 1), 'Course not found', 'Failed drop nonexistant course')

    #     # Variable
    #     s = {1: ['CMPSC132(3): Programming in Python II']}

    #     '''
    #         >>> s1.semesters
    #         {1: [CMPSC132(3): Programming in Python II]}
    #     '''
    #     self.assertEqual( s1.semesters, s, 'Failed to get semesters')

    #     # Variable
    #     s = {1: ['CMPSC132(3): Programming in Python II'], 2: ['No courses']}

    #     '''
    #         >>> s1.registerSemester()
    #         >>> s1.semesters
    #         {1: [CMPSC132(3): Programming in Python II], 2: [No courses]}
    #     '''
    #     s1.registerSemester()
    #     self.assertEqual( s1.semesters, s, 'Failed to get semesters')

    #     '''
    #         >>> s1.enrollCourse('CMPSC360', C, 2)
    #         'Course added successfully'
    #     '''
    #     self.assertEqual( s1.enrollCourse('CMPSC360', C, 2), 'Course added successfully', 'Failed to add course')

    #     # Variable
    #     s = {1: ['CMPSC132(3): Programming in Python II'], 2: ['CMPSC360(3): Discrete Mathematics']}

    #     '''
    #         >>> s1.semesters
    #         {1: [CMPSC132(3): Programming in Python II], 2: [CMPSC360(3): Discrete Mathematics]}
    #     '''
    #     self.assertEqual( s1.semesters, s, 'Failed to get semesters')

    # def test_studentAccount(self):
    #     '''
    #         >>> C = Catalog()
    #         >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
    #         'Course added successfully'
    #         >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
    #         'Course added successfully'
    #         >>> C.addCourse('MATH 230', 'Calculus', 4)
    #         'Course added successfully'
    #         >>> C.addCourse('PHYS 213', 'General Physics', 2)
    #         'Course added successfully'
    #         >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
    #         >>> s1.registerSemester()
    #         >>> s1.enrollCourse('CMPSC132', C,1)
    #         'Course added successfully'
    #         >>> s1.account.balance
    #         3000
    #         >>> s1.enrollCourse('CMPSC360', C, 1)
    #         'Course added successfully'
    #         >>> s1.account.balance
    #         6000
    #         >>> s1.enrollCourse('MATH 230', C,1)
    #         'Course added successfully'
    #         >>> s1.enrollCourse('PHYS 213', C,1)
    #         'Course added successfully'
    #         >>> print(s1.account)
    #         Name: Jason Lee
    #         ID: jl2890
    #         Balance: $12000
    #         >>> s1.account.chargeAccount(100)
    #         12100
    #         >>> s1.account.balance
    #         12100
    #         >>> s1.account.makePayment(200)
    #         11900
    #         >>> s1.getLoan(4000)
    #         >>> s1.account.makePayment(5000, 27611)
    #         'Loan Balance: 4000'
    #         >>> s1.account.makePayment(3000, 27611)
    #         8900
    #         >>> s1.account.loans
    #         {27611: Balance: $1000}
    #     '''

    # ! DONE
    def test_createStudent(self):

        p = Person('Jason Smith', '221-11-2629')
        s = createStudent(p)  
        self.assertEqual(str(s), 'Student(Jason Smith, js2629, Freshman)', 'Failed to get __str__')

if __name__ == '__main__':
    
	unittest.main(exit=False)
