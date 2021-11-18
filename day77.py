username="123@gmail.com"
passcod="1234"
user=input("enter your username:")
pass1=input("enter your password")
if user==username:
    if pass1==passcod:
        print("done")
    else:
        print("pass is incorrect")
else:
    print("username is incorrect")