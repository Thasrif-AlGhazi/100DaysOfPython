def is_valid(username, password):
   
    if username == 'admin' or (username == 'user' and password == 'qweasd'):
        return True
    else:
        return False

userr = input("Enter username: ")
pwd = input("Enter password: ")

result = is_valid(userr, pwd)

if result:
    print("Login Successful")
else:
    print("Login Failed")
