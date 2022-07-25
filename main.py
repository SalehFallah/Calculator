def password_validation(password):
    if len(password) < 8:
        print('your Password must be at least 8 character !!')
    elif password.isnumeric():
        print('Your Password must include at least one Character !!')
    elif password.isalpha():
        print('Your Password must include at least one Number !!')
    elif password.islower():
        print('Your password must include at least one Capital Character !!')
    else:
        print('Your Password is ', password, 'now you can SIGN IN !!')


while True:
    password = input('Please Choose a Password: ')
    password_validation(password)
    break
