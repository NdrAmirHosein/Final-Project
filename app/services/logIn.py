from app.handler.logIn import logIn
def login():
    try:
        national_code = input("Enter Your National Code: ")
        password = input("Enter Your Password: ")
        check = logIn(national_code, password)
    except ValueError as e:
        print(e)


    if check[0]:
        print(f"   Login successful! Welcome {check[1]}\n")
        return True
    else:
        print("\nError Log in...!\nPassWord IS Wrong!\n")