def password_validator(my_string: str) -> bool:
    """This function will validate if username and password contains
        at least one upper character, symbol and check that len is more than 6"""
    if my_string.isalnum() and not my_string.islower():
        char_in_string = False
        for char_check in my_string:
            if char_check.isalpha():
                char_in_string = True
        if char_in_string and len([*my_string]) > 6:
            return True
        return False


def username_validator(dictionary_check, check_username: str) -> bool:
    if check_username not in dictionary_check:
        return True
    return False


def user_registration(user_dictionary) -> dict:
    """This function will return new list with registered username with valid username and passwords"""
    new_dictionary = user_dictionary
    print("Register")

    username_exist = False
    while not username_exist:
        username = input("Username: ")
        username_exist = username_validator(new_dictionary, username)
        if not username_exist:
            print("This username already exist!")

    strength_password = False
    while not strength_password:
        password = input("Password: ")
        strength_password = password_validator(password)
        if not strength_password:
            print("Your password must contain at least one upper character or symbol!")

    if strength_password and username_exist:
        new_dictionary[username] = hash(password)

    return new_dictionary


def user_login(login_dictionary: dict) -> bool:
    check_dictionary = login_dictionary
    login_username = input("Username: ")
    login_password = hash(input("Password: "))
    if login_username in check_dictionary.keys():
        if check_dictionary[login_username] == login_password:
            print(f"Greetings {login_username} your login was successful!\n Welcome to User Authentication Application")
            return True
    print("You have entered an invalid username or password.\n Please try again!")
    return False


print("\nWelcome to User Authentication - app!\n"
      "Choose option:\n"
      "     1. User Registration \n"
      "     2. User Login\n"
      "     3. User Profile\n"
      "     4. Exit\n")

user_credentials = {}
# In this dictionary, we will store user information, each key will be a username and his values will be password.
valid_login = False
while True:
    selector = input("Please select your choice: ")
    if not selector.isdigit() or 0 > int(selector) >= 4:
        print("Please choose valid option")
        continue
    selector = int(selector)

    if selector == 4:
        print("See you soon!")
        break
    elif selector == 1:     # Registration
        user_credentials = user_registration(user_credentials)

    elif selector == 2:
        valid_login = user_login(user_credentials)    # Login

    elif selector == 3:     # Profile
        if not valid_login:
            print("You must be logged in your profile first.")

        else:
            print("Your profile information is empty!") # Change password can be added.


