email=input("Enter Your Email")
if '@' in email:                                                                         #paste
                
password=input("Enter your password")

if email=="hit@gmail.com" and password=="1234":
                print("Welcome")
elif email=="hit@gmail.com" and password!="1234":
                print("Incorrect password")                                     #if password is incorrect
                password=input("Enter your password again")        #re enter password
                if password=="1234":
                                print("Welcome")
                else:
                                print("Incorrect credentials")
else:
                print("Incorrect credentials")
else:
                print("Maximum Attempts exceeded")
