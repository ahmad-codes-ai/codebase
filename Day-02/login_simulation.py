# Login Simulation with a nested retry attempt
email = 'ahmad@gmail.com'
pas = "Hello1234"

e = input("Enter Your email: ")
p = input("Enter Your pass: ")

if e == email and p == pas:
    print("Login Successfully")
elif e == email and p != pas:
    print("Incorrect Password plz try again")
    p = input("Enter your password again: ")
    if p == pas:
        print("Correct pass Welcome")
    else:
        print("Your password is still incorrect try again later")
else:
    print("Incorrect email or pass entered")
