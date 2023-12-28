# lets start with a welcome message

print('welcome to Calvin/s terminal!\n') # welcome message

# lets define registration

users = {} # we need to store users/passwords
def register():
    while True: # allows for continous entries until correct
        username = input('Please enter a desired user name: ')
        if username in users:
            print('user name already exist, try again')
            continue # once the if statement is not true, loop continue
        print('your user name has been saved\nNow its time to create a password')
        print('Below are the requirements for your password: at least two upper case letters\nthree lower case letters\nat least one digit')
        password_input = input('Please create your new password: ')
        if web_password(password_input) != 'password was accepted and saved':
            print('password not accepted, try again')
            continue
        users[username] = password_input # user info is not stored
        break # exit loop

def web_password(password):
    str_password = str(password)
    if not (8 <= len(str_password) <= 12):
        return "incorrect length of password"
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
        if upper_count >= 2 and lower_count >= 3 and digit_count >= 1:  # if meets requirement, pass the check. 
            return "password was accepted and saved" 


print(users)


