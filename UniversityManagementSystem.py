#University Management System

class person:   #Base Class
    def __init__(self,name,roll,mobile):
        self.name = name
        self.roll = roll
        self.mobile = mobile
        
class student(person):  #Derived class from 'class person'
    def __init__(self,name,roll,mobile,branch):
        self.branch = branch
        
        super().__init__(name,roll,mobile)
        #super() (a built-in function) provide's access to methods of base class from derived class
        
class professor(person):  #Derived class from base class
    def __init__(self,name,roll,mobile,subject):
        self.subject=subject
        
        super().__init__(name,roll,mobile)
        
class college:  #Actual required class with a constructor
    
    def __init__(self,name):    #A constructor
        self.name = name
        self.students = []
        self.professors = []
        
    def add_student(self,student): #Method to get required student details
        self.students.append(student)
        
    def add_professor(self,professor):  #Method to get/append required professor details
        self.professors.append(professor)
        
    def display_students(self): #Method to display student details
        print()
        
        for i in range(len(self.students)):
            print(f"Student {i+1} Details")
            print(f"Name: {self.students[i].name}")
            print(f"Roll Number: {self.students[i].roll}")
            print(f"Mobile Number: {self.students[i].mobile}")
            print(f"Branch: {self.students[i].branch}")
            print()
            
    def display_professors(self):  #Method to display professor details
        print()
        
        for i in range(len(self.professors)):
            print(f"Professor {i+1} Details")
            print(f"Name: {self.professors[i].name}")
            print(f"Roll Number: {self.professors[i].roll}")
            print(f"Mobile Number: {self.professors[i].mobile}")
            print(f"Subject: {self.professors[i].subject}")
            print()

#To get details by user input
            
colleges = [] #Considering an Empty list,to append details accordingly

while True:
    #Providing a list of options to select
    
    print(('-'*10)+"\n\tchoose your option")
    print("1. Create a College")
    print("2. Add a Student info")
    print("3. Add a Professor info")
    print("4. Display students Details")
    print("5. Display Professors Details")
    print("6. Exit\n"+('-'*10))
    
    x = int(input("Enter your option: ")) #Taking Input from the user to select an option

    #Actions to be done, according to selected option
    
    if x == 1:
        cname = input("Enter College Name: ")
        x = True
        for i in colleges:
            if i.name == cname:
                x = False
                break
        if x == True:
            c = college(cname)
            
            colleges.append(c)  #append's details to the empty list named 'colleges'

            print("\nCollege Created Successfully")

        else:
            print(f"\n{cname} College already Exists")
            
    elif x==2:
        cname = input("Enter College Name: ")
        x = False
        for i in colleges:
            if i.name == cname: #checking given college name
                x = True
        if x  == True: #Getting further required details,if input college exists
            ind  = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    ind  = i
            sname = input("Enter Student name: ")
            sroll = input("Enter Roll number: ")
            smobile = input("Enter Mobile Number: ")
            sbranch = input("Enter student Branch: ")
            
            s1 = student(sname,sroll,smobile,sbranch)
            
            '''Adding student details to the cosidered above add_student method
            in college class'''
        
            colleges[ind].add_student(s1)
            
            print(f"\n{sname} added to {cname} college")
            
        else:
            print(f"\n{cname} College not exists")
            
    elif x == 3:
        cname = input("Enter College Name: ")
        x = False
        for i in colleges:
            if i.name == cname:
                x = True
                
        #Getting professor details from user,If input college exists
                
        if x == True:
            ind = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    ind = i
            tname = input("Enter Professor name: ")
            troll = input("Enter Roll number: ")
            tmobile = input("Enter Mobile Number: ")
            tsubject = input("Entr Subject: ")

            t1 = professor(tname,troll,tmobile,tsubject)

            '''Adding professor details to the considered above add_professor method
            in college class'''

            colleges[ind].add_professor(t1)
            
            print(f"\n{tname} added to {cname} college")
        else:
            print(f"\n{cname} college not exists")

    elif x == 4:
        cname = input("Ener college name: ")
        x = False
        for i in colleges:
            if i.name == cname:
                x= True
        if x == True:
            ind = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    ind = i

            '''Displaying all student details that are previously appended
            in add_student method from college class'''

            colleges[ind].display_students()
            
        else:
            print(f"{cname} College not exists")

    elif x == 5:
        cname = input("Enter college name: ")
        x = False
        for i in colleges:
            if i.name == cname:
                x = True
        if x == True:
            ind = -1
            for i in range(len(colleges)):
                if colleges[i].name == cname:
                    ind = i
                    
            '''Displaying all professor details that are previously appended
            in add_professor method from college class'''
                    
            colleges[ind].display_professors()    
            
        else:
            print(f"{cname} College not exists")

    elif x == 6:
        break
    
    else:
        print("Provide correct input\n"+('-'*10))











