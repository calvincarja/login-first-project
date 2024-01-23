# lets start with a welcome message

print('welcome to Calvin/s terminal!\n') # welcome message

# lets define registration

users = {} # we need to store username : password (key:value)
def register():
    while True: # allows for continous entries until correct
        username = input('Please enter a desired user name: ')
        if username in users:
            print('user name already exist, try again')
            continue # once the if statement is not true, loop continue
        print('your user name has been saved\nNow its time to create a password')
        print('Below are the requirements for your password: at least two upper case letters\nthree lower case letters\nat least one digit')
        password_input = input('Please create your new password: ')
        if web_password(password_input) != 'password was accepted and saved': # varible being passed through web_password function is local, it does not need to match the varible inside the web_password function outside this function
            print('password not accepted, try again')
            continue
        users[username] = password_input # user info is now stored
        break # exit loop

def web_password(password):
    while True:
        str_password = str(password)
        if not (8 <= len(str_password) <= 12):
            print("incorrect length of password, try again") 
            password = input('enter your password')
        upper_count = 0
        lower_count = 0
        digit_count = 0        
        for x in password:
            if x.isupper(): 
                upper_count += 1 # adds a 1 to each instance of upper == true
            if x.islower():
                lower_count += 1
            if x.isdigit():
                digit_count += 1
        if not (upper_count >= 2 and lower_count >= 3 and digit_count >= 1):  # if meets requirement, pass the check. 
            print('password did not meet requirements')  
            password = input('enter your password')       
        else:
            return "password was accepted and saved" # the password will be stored as a value to the username key
            break
        
    

def login ():
    while True:
        login_username = input('Please enter your username: ')
        if login_username not in users: # in keyword used with dictionarys only refernce keys, not values
            print('username is not in our system. Please try again: ')
            login_username = input('Please enter your username: ')
        else:
            print('Username found')
            break
    
    while True:
        login_password = input('Enter your password: ')
        if login_password != users[login_username]: # the password is the value of key:value relationship, thus, password is the value for usernsame key
            print('password is incorrect - try agian')
            login_password = input('Enter your password: ')
        else:
            print('correct password')
            break
    

def login_or_register ():
    valid_inputs = {'login', 'register'}
    while True:
        log_v_reg = input('Please type login or register: ').lower() # intialize lower case without new varible
        if log_v_reg not in valid_inputs:
            print('Invalid input. Please type either "login" or "register".')
        else:
            break
        if log_v_reg == 'login':
            login()
        elif log_v_reg == 'register':
            register()
        # i can also use if/else as only two options to pick