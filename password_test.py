import unittest
from password import User 

class TestUser(unittest.TestCase):
  '''
  Test class that defines the test cases for the user class behaviours

  Args:
    unittest.TestCase: TestCase class that helps in creating test cases
  '''

  def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_user = User("ro.fenty","banana22")
  
  def tearDown(self):
    '''
    tearDown method to clear after each test has run
    '''
    User.user_list = []
    