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
  



class Credentials:
  """
  Class that stores existing account credentials for the current user, 
  creates new accounts, and generates new password for outside apps
  """
  cred_list = []

  def __init__(self,account,user_name,password): #need to make it so each social media needs its own username and password 
    self.account = account
    self.user_name = user_name
    self.password = password 
  
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
  


  
  

