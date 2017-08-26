class Course(object):
    def __init__(self,name,fees):
        self.name = name
        self.fees = fees
    def CourseDetails(self):
        print("course name:"+self.name)
        print("fees:"+str(self.fees))

class Student(Course):
    def __init__(self,sname,cname,cfees):
        Course.__init__(self,cname,cfees)
        self.Studentname = sname

    def StudentDeatils(self):
        print("student name:"+self.Studentname)


ss=Student("mahendra","java",9000)
ss.CourseDetails()
ss.StudentDeatils()