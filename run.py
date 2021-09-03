from password import User, Credentials 

#User
def create_user(username,password):
  '''
  Function to create new user
  '''
  new_user = User(username,password)
  return new_user

def save_users(User): #should this be lowercase?
  '''
  Function to save new user
  '''
  User.save_user() #should this be lowercase?


#Credentials
def create_cred(account,user_name,password):
  '''
  Function that creates a new credential for current user account
  '''
  new_cred = Credentials(account,user_name,password)
  return new_cred


def save_credentials(credentials): #figure out if credentials needs to be uppercse first letter 
  '''
  Function to save credentials
  '''
  Credentials.save_cred()


def delete_credentials(credentials):
  '''
  Function to delete a credential
  '''
  Credentials.delete_cred()


def display_all_cred():
  '''
  Function that diplays all credentials of current user
  '''
  return Credentials.display_cred()


def main():





  





