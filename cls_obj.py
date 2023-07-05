"""
class Stud:
    srn=0
    name="NoName"
    st_cls="NoCls"
    electives=[]

    def __init__(self,name,srn,st_cls):
        self.srn=srn
        self.name=name
        self.st_cls=st_cls

    def add_elective(self,subj):
        self.electives.append(subj)

std=Stud("KP",97,"sem-2")


print(f"{std.srn=}")
print(f"{std.name=}")
print(f"{std.st_cls=}")

"""

class Student:

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def info(self):
        print(f"name:{self.name} | age:{self.age} | gender:{self.gender}")

s=Student("ram",19,"male")
s.info()
     
student_l=[("KP",19,"male"),("Dev",18,"female")]

students=[]
for name,age,gender in student_l:
    s=Student(name,age,gender,)
    s.info()
    



        






