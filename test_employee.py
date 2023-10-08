import unittest
from unittest.mock import patch
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
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
        
    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            
            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Nguyen/may")
            self.assertEqual(schedule, "success")            
            
            mocked_get.return_value.ok = False
            
            schedule = self.emp_1.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Nguyen/June")
            self.assertEqual(schedule, "Bad Response!")       
        
if __name__ == "__main__":
    unittest.main()