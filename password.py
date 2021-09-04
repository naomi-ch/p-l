import random
import string 

class User:
  """
  Class that generates new instance of user
  """
  user_list = []

  def __init__(self,username,password):
    self.username = username
    self.password = password 


  def save_user(self):
    '''
    save_user method saves new user objects to the user list
    '''
    User.user_list.append(self)
  
  @classmethod
  def user_exists(cls,name,password):

    for user in cls.user_list:
      if(user.username == name and user.password == password):
        return True
    return False
  



class Credentials: #must add classmethod to verify if user is in user list
  """
  Class that stores existing account credentials for the current user, 
  creates new accounts, and generates new password for outside apps
  """
  cred_list = []

  def __init__(self,account,user_name,cred_password): #need to make it so each social media needs its own username and password 
    self.account = account
    self.user_name = user_name
    self.cred_password = cred_password 
  
  def save_cred(self):
    '''
    save_cred method saves current user credentials to the cred_list
    '''
    Credentials.cred_list.append(self)
  
  def delete_cred(self):
    '''
    del_cred method deletes an account (current account) credentials from the cred_list
    '''
    Credentials.cred_list.remove(self)
  
  @classmethod
  def display_cred(cls):
    '''
    method thhat returns the cred_list (of current user???)
    '''
    return cls.cred_list
  
  def generate_password(passlength = 8): #why is 'i' not accessible
    '''
    generate a random password which are a string of letters, digits and special characters
    '''
   
    random_password = ''.join(random.choice(string.printable) for i in range(passlength))
    print("Your generated password:",random_password)



  
  

