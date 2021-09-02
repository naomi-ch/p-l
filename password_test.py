import unittest
from password import User,Credentials 


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
  
  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.username,"ro.fenty")
    self.assertEqual(self.new_user.password,"banana22")

  
  def test_save_user(self):
    '''
    test_init test case to test if user obj is saved into the user_list
    '''
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)
  


class TestCredentials(unittest.TestCase):
  '''
  Test class that defines the test cases for the credential class behaviours

  Args:
    unittest.TestCase: TestCase class that helps in creating test cases
  '''

  def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_cred = Credentials("Twitter","riri_fe","peanut4")
  
  def tearDown(self):
    '''
    tearDown method to clear after each test has run
    '''
    Credentials.cred_list = []
  
  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_cred.account,"Twitter")
    self.assertEqual(self.new_cred.user_name,"riri_fe")
    self.assertEqual(self.new_cred.password,"peanut4")

  def test_save_cred(self):
    '''
    test_init test case to test if credentials is saved into cred_list
    '''
    self.new_cred.save_cred()
    self.assertEqual(len(Credentials.cred_list),1)
  
  def test_save_multiple_cred(self):
    '''
    tests if we can save multiple credentials into cred_list
    '''
    self.new_cred.save_cred()
    test_cred = Credentials("Gmail","r.f@gmail.com","coconut44")
    test_cred.save_cred()
    self.assertEqual(len(Credentials.cred_list),2)

  def test_delete_cred(self):
    '''
    test_if we can remove cred account from cred list
    '''
    self.new_cred.save_cred()
    test_cred = Credentials("Gmail","r.f@gmail.com","coconut44")
    test_cred.save_cred()

    self.new_cred.delete_cred()
    self.assertEqual(len(Credentials.cred_list),1)
  
  def test_display_cred(self):
    '''
    test if it can return a list of creds saved to cred_list
    '''

    self.assertEqual(Credentials.display_cred(),Credentials.cred_list)




if __name__ == '__main__':
    unittest.main()