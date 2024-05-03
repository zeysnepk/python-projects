#User Login Program with while loop

print("""
*******************************
        USER LOGİN
*******************************
""")

sys_username = "zeysnepk"
sys_password = "1234"

access_count = 3

while True:
    input_username = input("User Name : ")
    input_password = input("Password : ")

    if input_username == sys_username and input_password != sys_password:
        print("!Incorrect Password! please try again\n")
        access_count -= 1
    elif input_username != sys_username and input_password == sys_password:
        print("!Incorrect Username! please try again\n")
        access_count -= 1
    elif input_username != sys_username and input_password != sys_password:
        print("!Incorrect Login! please try again\n")
        access_count -= 1
    else:
        print("!Login Successful!")
        break

    if access_count == 0:
        print("Your right of access has expired")
        break



