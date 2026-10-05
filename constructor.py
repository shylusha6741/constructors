#                Example:Bank
class Bank:
    bank_name="SBI"
    branch_name="warangal"
    def __init__(self,account_no,customer_name,balance,account_type):
        self.account_no=account_no
        self.customer_name=customer_name
        self.balance=balance
        self.account_type=account_type
    def displayDetails(self):
        print("Bank Name:",Bank.bank_name)
        print("Branch Name:",Bank.branch_name)
        print("Account Number:",self.account_no)
        print("Customer Name:",self.customer_name)
        print("Balance:",self.balance)
        print("Account Type:",self.account_type)

c1=Bank(7815,"Shylusha",25000,"Savings")
c2=Bank(6875,"Teju",80000,"Current")
c3=Bank(4567,"Mouna",70000,"Savings")
print("------customer1 details-----")
c1.displayDetails()
print("------customer2 details-----")
c2.displayDetails()
print("------customer3 details-----")
c3.displayDetails()
_________________________________________________________________________________
#               Example:Movie
class Movie:
    industry="Tollywood"
    language="Telugu" 

    def __init__(self,movie_name,hero,director,rating):
        self.movie_name=movie_name
        self.hero=hero
        self.director=director
        self.rating=rating
    def displayDetails(self):
        print("Industry:",Movie.industry)
        print("Language:",Movie.language)
        print("Movie Name:",self.movie_name)
        print("Hero",self.hero)
        print("Director",self.director)
        print("Rating:",self.rating)
m1=Movie("RRR","Ram Charan","s.s Rajamouli",9.0)
m2=Movie("Pushpa","Allu Arjun","Sukumar",8.5)
m3=Movie("Baahubali","Prabhas","S.S.Rajamouli",9.2)
print("-------Movie1 details------")
m1.displayDetails()
print("-------Movie2 details------")
m2.displayDetails()
print("-------Movie3 details------")
m3.displayDetails()

#________________________________________________________________________________________________________
#                             Example:Employee
class Employee:
    company_name="TCS"
    company_location="Hyderabad"

    def __init__(self,employee_id,employee_name,department,salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.department=department
        self.salary=salary
    def displayDetails(self):
        print("Company Name:",Employee.company_name)
        print("Company Location:",Employee.company_location)
        print("Employee ID:",self.employee_id)
        print("Employee Name:",self.employee_name)
        print("Department:",self.department)
        print("salary:",self.salary)

e1=Employee(101,"Shylu","IT",50000)
e2=Employee(102,"Saipriya","HR",40000)
e3=Employee(103,"Sweety","Finance",45000)

print("--------employee1 details-----")
e1.displayDetails()
print("--------employee2 details-----")
e2.displayDetails()
print("--------employee3 details-----")
e3.displayDetails()