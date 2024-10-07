lists = [
    {
        "email": "shaikmaheer123@gmail.com",
        "password": "1111a!",
        "balance": 1200000
    },
    {
        "email": "heeru123@mail.com",
        "password": "1111a!",
        "balance": 1330022
    },
    {
        "email": "mahee123@gmail.com",
        "password": "1111a!",
        "balance": 113011
    },
    {
        "email": "heer123@gmail.com",
        "password": "1111a!",
        "balance": 1112000
    },
    {
        "email": "shaik123@gmail.com",
        "password": "1111a!",
        "balance": 1114000
    }
]
def isalpha(x):
    a =x[-1:-4:-1] 
    return a.isalpha()
def lett_dig_symbol(password):
    special_characters = "~!@#$%^&*()_+=<>,.?/:;\|{}[]"
    special_char = False
    digit = False
    letter = False
    for i in password:
        if i in special_characters:
            special_char = True
        elif i.isdigit():
            digit = True
        elif i.isalpha():
            letter = True
    return special_char and digit and letter

def signup():
    print("To signup, you must enroll with a new email and password")
    print("Example: shaikmaheer713@gmail.com or shaikmaheer123_@foundation.org")
    email_signup = input("Enter Email: ")
    turns = 3
    while turns>0:
        if len(email_signup) < 321 and len(email_signup) > 3 and lett_dig_symbol(email_signup) and isalpha(email_signup):
            print("EMAIL SUCCESSFULLY CREATED")
            break
        else:
            print("OOPS.. Your Email doesn't meet our requirements")
            turns = turns -1
            if turns == 0:
                print("chances are over")
                quit()
            else:
                email_signup = input("Enter Email: ")
    password_signup = input("Enter Password: ")
    turns = 3
    while turns>0: #while TRUE 
        if len(password_signup) >= 6 and len(password_signup) < 63 and lett_dig_symbol(password_signup):
            print("PASSWORD SUCCESSFULLY CREATED")
            lists.append({"email": email_signup, "password": password_signup, "balance": 0})  # Add user to lists
            break
        
        else:
            print("OOPS..Your password doesn't meet our requirements")
            turns = turns -1
            if turns == 0:
                print("Chances are over")
                quit()
            else:
                password_signup = input("Enter Password: ")
def signin():
    print("To sign in you must enter your details")
    email_enter = input("ENTER EMAIL:")
    found_user = False
    for user in lists:
        if email_enter == user["email"]:
            found_user = True
            password_enter = input("enter password:")
            if password_enter == user["password"]:
                print("You are now signed in")
                next_step = input("Choose action:\n    1. Add money\n    2. Check balance\n    3. Send money\n    4. Withdraw cash\nEnter your choice (1/2/3/4): ")
                if next_step == "1":
                    amount = int(input("Enter the amount to add: "))
                    user['balance'] += amount
                    print(f"Amount added successfully. Your new balance is: {user['balance']}")
                elif next_step == "2":
                    print(f"Your current balance is: {user['balance']}")
                elif next_step == "3":
                    money_send_person = input("Enter the email of the person whom you want to send the money:")
                    for j in lists:
                        if money_send_person == j['email']:
                            print("We have found their details")
                            amount_money = int(input(f"Enter the amount that you want to send: "))
                            if amount_money <= user['balance']:
                                user['balance'] -= amount_money
                                j['balance'] += amount_money
                                print("Amount successfully sent!!")
                                print(f"Your current balance is {user['balance']}")
                            else:
                                print("Insufficient balance")
                                quit()
                    else:
                        print("Given details are invalid/doesn't exist")
                elif next_step == "4":
                    with_draw_amount = int(input("enter amount you want to withdraw: "))
                    if with_draw_amount <= user['balance']:
                        user['balance'] -= with_draw_amount
                        print(f"Your current balance is: {user['balance']}")
                    else:
                        print("Insufficient amount")
                else:
                    print("Invalid choice")
            else:
                print("Incorrect password")
                quit()  # No need to continue looping once the user is found
    if not found_user:
        print("Your email doesn't exist")
        again1 = input("Do you want to signup(Y/N): ")
        if again1.lower() == "y":
            signup()
        else:
            print("THANK YOU FOR VISITING..........")

print("...............welcome.................")
signing_choose = input("Choose one: \n       1.signin\n       2.signup:")
print(f"You chose {signing_choose} ")
if signing_choose.lower() == "signin" or signing_choose == "1":
    signin()
    

elif signing_choose.lower() == "signup" or signing_choose == "2":
    signup()
    again = input("Do u want to signin again(Y/N): ")
    if again.lower() =="y":
        signin()
    else:
        print("THANK YOU FOR VISITING..............")

else:
    print("You chose invalid option")
    quit()
