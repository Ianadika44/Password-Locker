#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(f_name, l_name, password, email):
    '''
    Function to create a new user
    '''
    new_user = User(f_name, l_name, password, email)
    return new_user


def save_users(user):
    '''
    Function to save user detail
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete a user detail
    '''
    user.delete_user()


def find_user(name):
    '''
    Function that finds a user by name and returns the details
    '''
    return User.find_by_name(name)


def check_existing_users(name):
    '''
    Function that check if a user exists with that name and return a Boolean
    '''
    return User.user_exist(name)


def display_user():
    '''
    Function that returns all the saved details
    '''
    return User.display_user()


def main():
    print("Hello Welcome to your account. What is your name?")
    user_name = input()

    print(f"Hello.{user_name} what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the account,I ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New User")
            print("-"*100)

            print("First name ....")
            f_name = input('First Name:')
            print('\n')

            print("Last name ...")
            l_name = input('Last Name:')
            print('\n')

            print("Password ...:")
            password = input('Password:')
            print('\n')

            print("Email address ...")
            email = input('Email:')
            print('\n')

            # create and save new user.
            save_users(create_user(
                f_name, l_name, password, email))
            print('\n')
            print(f"New User {f_name} {l_name} created")
            print(
                f"You can now login to your {f_name} account using your password.")
            print('\n')
            
        elif short_code == 'dc':

            if display_user():
                print("Here is a list of all your details")
                print('\n')

                for user in display_user():
                    print(
                        f"{user.account_name} {user.user_name} .....{user.password}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any details saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the password to log in")

            search_user = input()
            if check_existing_users(search_user):
                search_user = find_user(search_user)
                print(f"search_user{f_name} {l_name}")
                print('-' * 20)

                print(f"search_user.......{password}")
                print(f"search_user.......{email}")
            else:
                print("That user does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()
