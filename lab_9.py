##Q.1
# class bank_account:
#     def data(self,name,ac_number,ac_type,balance=0):
#         self.name=name
#         self.ac_number=ac_number
#         self.ac_type=ac_type
#         self.balance=balance
#     def deposit(self,a):
#         if a>0:
#             self.balance+=a
#     def withdraw(self,w):
#         self.balance-=w
#     def display(self):
#         print(f"name={self.name}\naccount number={self.ac_number}\naccount type={self.ac_type1}\nbalance={self.balance}")
# v=bank_account()
# while 1:
#     c=int(input("1.New customer\n2.Deposit\n3.Withdraw\n4.Display\n5.Exit\n:"))
#     if c==1:
#         v.data(name=input("enter a name:"),ac_number=input("enter a account number:"),ac_type=input("enter a account type:"))
#     if c==2:
#         v.deposit(a=int(input("enter a amount to deposit:")))
#     if c==3:
#         v.withdraw(w=int(input("enter a amount to withdraw:")))
#     if c==4:
#         v.display()
#     if c==5:
#         break

##Q.2
# print("Library Mangement System")
# class Book:
#     def __init__(self,title,author,year_attributes):
#         self.title=title
#         self.author=author
#         self.year_attribute=year_attributes
#     def __str__(self):
#         return f"{self.title} by {self.author} {self.year_attribute}"
#
# class library:
#     def __init__(self):
#         self.books=[]
#
#     def add_book(self,title,autor,year):
#         n=Book(title,autor,year)
#         self.books.append(n)
#         #print(n)
#
#     def view_book(self):
#         if not self.books:
#             print("NONE")
#         else:
#             print("BOOKS IN LIBRARY ARE")
#             for i in self.books:
#                 print(i)
#     def serch_book(self,title):
#         for i in self.books:
#             if i.title.lower()==title.lower():
#                 print(f"Book:{i}")
#                 break
#             else:
#                 print("sorry")
#
# def meanu():
#     print("1.Add Book\n2.View All Books\n3.Search Book By Title\n4.Exit")
#
# lib=library()
# while 1:
#     meanu()
#     c=int(input(":"))
#     if c==1:
#         name=input("enter a book name")
#         author=input("enter a author name")
#         year=input("enter a year")
#         if year.isdigit():
#             lib.add_book(name,author,int(year))
#     if c==2:
#         lib.view_book()
#     if c==3:
#         lib.serch_book(title=input("enter a tittle"))
#     if c==4:
#         break
##Q.3
# print("Employee Management System")
# class Employee:
#     def __init__(self,id,name,salary):
#         self.id=id
#         self.name=name
#         self.salary=salary
#     def update(self,name=None,salary=None):
#         if name:
#             self.name=name
#         if salary:
#             self.salary=salary
#     def __str__(self):
#          return f"ID:{self.id} name: {self.name} salary: {self.salary}"
# class mang:
#     def __init__(self):
#         self.empoly={}
#     def add(self,id,name,salary):
#         if id in self.empoly:
#             print("Id is alredy enrolled")
#             return
#         n=Employee(id,name,salary)
#         self.empoly[id]=n
#
#     def view_emp(self):
#        if not self.empoly:
#            print("NONE")
#        else:
#            print("Empolyess are")
#            for i in self.empoly.values():
#                print(i)
#     def update(self,id,name,salary):
#         emp=self.empoly[id]
#         emp.update(name=name or None,salary=salary if salary else None)
#
#     def deal(self,id):
#         del self.empoly[id]
# m=mang()
# while 1:
#     y=int(input("1.Add Employess\n2.View all Employees\n3.Update Employee Informatiom\n4.Delete Employee\n5.exit\n:"))
#     if y==1:
#         m.add(name=input("enter a name:"),id=input("enter a id:"),salary=input("enter a salary in Rs:"))
#     if y==2:
#         m.view_emp()
#     if y==3:
#         m.update(id=input("enter a id:"),name=input("enter a name:"),salary=input("enter a salary:"))
#     if y==4:
#         m.deal(id=input("enter a id which you want to delate:"))
#     if y==5:
#         break


##Q.4
# class person:
#     def __init__(self,name,code):
#         self.name=name
#         self.code=code
# class Accunt(person):
#     def __init__(self,name,code,member_pay):
#         person.__init__(self,name,code)
#         self.member_pay=member_pay
# class Admin(person):
#     def __init__(self,name,code,experince):
#         person.__init__(self,name,code)
#         self.experiance=experince
# class Employee(Accunt,Admin):
#     def __init__(self,name,code,member_pay,experince):
#         Accunt.__init__(self,name,code,member_pay)
#         Admin.__init__(self,name,code,experince)
#     def display(self):
#         print(f"name:{self.name}\ncode:{self.code}\nmember_pay:{self.member_pay}\nexperince:{self.experiance}year")
# e=Employee("yash","ed4358-3001",50000,62)
# e.display()

##Q.5
# class staff:
#     def __init__(self,code,name):
#         self.code=code
#         self.name=name
#     def dis(self):
#         print(f"staff code:{self.code} name:{self.name}")
# class teacher(staff):
#     def __init__(self,code,name,subject,publication):
#         staff.__init__(self,code,name)
#         self.subject=subject
#         self.publication=publication
#     def dis(self):
#         print(f"teacher code:{self.code} name:{self.name} subject:{self.subject} publiction:{self.publication}")
# class typist(staff):
#     def __init__(self,code,name,spped):
#         staff.__init__(code,name)
#         self.speed=spped
#     def dis(self):
#         print(f"typist:{self.code} name:{self.name} speed:{self.speed}")
#
# class officer(staff):
#     def __init__(self,code,name,grade):
#         staff.__init__(self, code, name)
#         self.grade=grade
#     def dis(self):
#         print(f"officer:{self.code} name:{self.name} grade:{self.grade}")
#
# class regular(typist):
#     def __init__(self,code,name,speed,salary):
#         typist.__init__(self,code,name,speed)
#         self.salary=salary
#     def dis(self):
#         print(f"regular typist:{self.code} name:{self.name} speed:{self.speed} salary:{self.salary}")
# class casual(typist):
#     def __init__(self,code,name,speed,daily_wages):
#         typist.__init__(self,code,name,speed)
#         self.daily_wages=daily_wages
#     def dis(self):
#         print(f"casual typist:{self.code} name:{self.name} speed:{self.speed} dalily wages:{self.daily_wages}")
#
# while 1:
#     l=int(input("1.Teacher\n2.Officer\n3.Regular Typist\n4.Casaul typist\n5.Exit\n:"))
#     if l==1:
#         a=teacher(code=input("enter a code:"),name=input("enter a name:"),subject=input("enter subject:"),publication=input("enter a publication:"))
#         a.dis()
#     if l==2:
#         a=officer(code=input("enter a code:"),name=input("enter a name:"),grade=input("input a grade A/B/C:"))
#         a.dis()
#     if l==3:
#         a=regular(code=input("enter a code:"),name=input("enter a name:"),speed=int(input("enter a speed in wps:")),salary=int(input("enter a salary in int form")))
#         a.dis()
#     if l==4:
#         a=casual(code=input("enter a code:"),name=input("enter a name:"),speed=int(input("enter a speed in wps:")),daily_wages=int(input("enter a salary in int form")))
#         a.dis()
#     if l==5:
#         break
def add(a,b):
    print(a+b)
a=(add,10,12)
print(a)























