class Employee:

    def __init__(self,name,address):
        self.ename=name
        self.eaddress=address
    def show(self):
        print("Employee name:",self.ename)
        print("You are from :",self.eaddress)


emp1=Employee('Raj','Kolkata');
emp1.show();
emp2=Employee('Soumya','Howrah');
emp2.show();
nm=raw_input("Enter Employee name:")
addr=raw_input("Enter Employee name:")
emp3=Employee(nm,addr)
emp3.show()


    

        
