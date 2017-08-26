class Employee:
    def __init__(self,name,address):
        self.ename=name
        self.eaddress=address
    def show(self):
        print("employee name:{} \t your address:{}".format(self.ename,self.eaddress))
    
elist=[]
no_of_employee=int(input("number of employee"))
for i in range(no_of_employee):
    nm=input("enter the nmae:")
    adr=input("enter the address")
    emp1=Employee(nm,adr)
    elist.append(emp1)
    emp1.show()

for i in elist:
    i.show()
