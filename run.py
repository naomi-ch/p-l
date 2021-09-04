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

def save_users(user): #should this be lowercase?
  '''
  Function to save new user
  '''
  user.save_user() #should this be lowercase?

def check_user(name,password):
  '''
  Function that checks if user exists and then logs them in
  '''
  return User.user_exists(name,password)



#Credentials
def create_cred(account,user_name,cred_password):
  '''
  Function that creates a new credential for current user account
  '''
  new_cred = Credentials(account,user_name,cred_password)
  return new_cred


def save_credentials(credentials): #figure out if credentials needs to be uppercse first letter 
  '''
  Function to save credentials
  '''
  credentials.save_cred()


def delete_credentials(credentials):
  '''
  Function to delete a credential
  '''
  credentials.delete_cred()


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
      username = input("Create Username: ")

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
      print('\n')
      print("Proceed to login")
      print("-"*85)
      current_user = input("Username: ")
      current_password = input("Password: ")

      while current_user != username or current_password != password:
        print("Invalid Username or Password")
        current_user = input("Username: ")
        current_password = input("Password: ")
      else:
        print(f"Welcome {current_user} to your Password-Locker account!")

    elif user_input == 'lg':
      print("Login page")
      print("-"*20)
      username = input("Enter Username: ")
      password = input("Enter Password: ")
      check = check_user(username,password)

      if check == check_user(username,password):
        print('\n')
        print(f"Hello {username}! Welcome back to Password-Locker\n")
      else:
        print("User does not exist, please create an account")

    while True:
      '''
      Loop through functions after login in
      '''
      print("""\nUse these short codes to manage your credentials:\n
      ac: add a credential \n
      dc: display credentials \n
      cg: create a credential with a generated password \n
      q: quit""")
      print('\n')
      user_input = input().lower()

      if user_input == 'ac':
        print('\n')
        print("Add an account")
        print("-"*20)

        account = input("Account: ")
        user_name = input("Account Username: ")
        cred_password = input("Account Password: ")

        #save credential
        save_credentials(create_cred(account,user_name,cred_password))
        print('\n')
        print(f"{account} credentials have been saved.")
          
      elif user_input == 'dc':
        '''
        Displaying credentials
        '''
        if display_all_cred():
          print('\n')
          print(f"{username}'s credentials:")
          print("-"*20)

          for account in display_all_cred():
            print(f"Account: {account} \nUsername: {user_name}\nPassword: {cred_password}")
            print("-"*20)
          else:
            print("There are no accounts to display")



      





      '''
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

  





