import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="logEmployee.log"
)

class Employee:
    """A sample Employee class"""
        
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logging.info("created Employees: {} - {}".format(self.fullname, self.email))
                
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    
emp_1 = Employee("Long", "Nguyen")
emp_2 = Employee("Khanh", "Nguyen")
emp_3 = Employee("Thanh", "Nguyen")
