class Course:
    """
    A class that provides methods to print out the  head office location, course name and a webpage to contact the publisher of the course.
    """
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office_location = "Cape Town"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office(self):
        print("If you would like to visit us in person our head office is located in ", self.head_office_location)


class OOPCourse(Course):
    """
    A subclass that inherits from Course.
    It provides additional methods to print the course trainer, course id and a course description.
    """
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"
        self.course_id = '#12345'

    def trainer_details(self):
        print("This course is about ", self.description, "and your assigned trainer will be ", self.trainer)

    def show_course_id(self):
        print("Course ID:", self.course_id)


course_1 = OOPCourse()  # declares an object with the OOPCourses class
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
