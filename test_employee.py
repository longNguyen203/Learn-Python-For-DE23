import unittest
from  Employee import Employee

class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    
    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Long", "Nguyen", 50000)
        self.emp_2 = Employee("Khanh", "Nguyen", 60000)
    
    def tearDown(self):
        print("tearDown\n")
    
    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Long.Nguyen@gmail.com")
        self.assertEqual(self.emp_2.email, "Khanh.Nguyen@gmail.com")

        self.emp_1.first = "Quynh"
        self.emp_2.first = "Thanh"
        
        self.assertEqual(self.emp_1.email, "Quynh.Nguyen@gmail.com")
        self.assertEqual(self.emp_2.email, "Thanh.Nguyen@gmail.com")
        
    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Long Nguyen")
        self.assertEqual(self.emp_2.fullname, "Khanh Nguyen")
        
        self.emp_1.first = "Quynh"
        self.emp_2.first = "Thanh"
        
        self.assertEqual(self.emp_1.fullname, "Quynh Nguyen")
        self.assertEqual(self.emp_2.fullname, "Thanh Nguyen")
        
    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 50001)
        self.assertEqual(self.emp_2.pay, 60001)
        
if __name__ == "__main__":
    unittest.main()