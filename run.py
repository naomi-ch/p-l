from password import User, Credentials 
'''
1. Create user, save user
2. If Wrong input: "Sorry please enter correct short code" - if not check_input
2. Or log in user
3. If user is logged in, select from these short codes - if not check_input print pls input correct short code [short codes]
4. If user: add credential, delete credential, display credentials, find creds(?)
5. If add credential: trigger create_cred func(input account,username,password), trigger save cred func, then display cred
6. If delete credential: trigger delete_credentials func - print credential deleted
7. If display credential: trigger display_all_cred func - print "your credentials"
8. If exit: trigger exit func (create exit func) - print "Goodbye!"

'''

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

def password_random():
  '''
  Function that generates a random password
  '''
  given_password = Credentials.generate_password()
  return given_password


def main():

  while True:
    print("Hello Welcome to Password Locker!")
    print("Select a short code to use the application: ") 
    print("To log into your account: 'lg', To create a new account: 'ca'")
    user_input = input().lower()
    print('\n')

    if user_input == 'ca':
      print("Create Username")
      username = input()

      while True:
        print("Enter 'tp' to create your own password:\nEnter 'gp' to generate a random password")
        type_password = input()
        if type_password == 'tp':
          password = input("Enter password:")
          break
        elif type_password == 'gp':
          password = password_random()
          break
        else:
          print("Invalid password, please try again")
      
      save_users(create_user(username,password))
      print("*"*85)
      print(f"Welcome {username}! You've successfully created a Password-Locker account!")
      print("*"*85)
      '''




      print("Create Password")
      new_password = input()

      print("Confrm Password")
      confirm_password = input()

      while confirm_password != new_password:
        print("Passwords must match. Please try again.")
        print("Create Password")
        new_password = input()
        print("Confirm Password")
        confirm_password = input()

      else:
        print(f"Welcome {new_user}!")
        print("Log into your account")
        print("Enter Username")

      '''
    ''' 
    if user_input == 'lg':
      print("Enter Username")
      current_user = input()

      print("Enter Password")
      current_user_password = input()
    

    '''
    break




if __name__ == '__main__':
  main()

  





