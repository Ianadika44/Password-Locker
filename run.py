#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(f_name, l_name, password, email):
    '''
    Function to create a new user
    '''
    new_user = User(f_name, l_name, password, email)
    return new_user


# def save_users(user):
#     '''
#     Function to save user detail
#     '''
#     user.save_user()


# def del_user(user):
#     '''
#     Function to delete a user detail
#     '''
#     user.delete_user()


# def find_user(name):
#     '''
#     Function that finds a user by name and returns the details
#     '''
#     return User.find_by_name(name)


# def check_existing_users(name):
#     '''
#     Function that check if a user exists with that name and return a Boolean
#     '''
#     return User.user_exist(name)


# def display_user():
#     '''
#     Function that returns all the saved details
#     '''
#     return User.display_user()


# def main():
#     print("Hello Welcome to your contact list. What is your name?")
#             user_name = input()

#             print(f"Hello {user_name}. what would you like to do?")
#             print('\n')

#             while True:
#                     print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

#                     short_code = input().lower()

#                     if short_code == 'cc':
#                             print("New Contact")
#                             print("-"*10)

#                             print ("First name ....")
#                             f_name = input()

#                             print("Last name ...")
#                             l_name = input()

#                             print("Phone number ...")
#                             p_number = input()

#                             print("Email address ...")
#                             e_address = input()


#                             save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
#                             print ('\n')
#                             print(f"New Contact {f_name} {l_name} created")
#                             print ('\n')

#                     elif short_code == 'dc':

#                             if display_contacts():
#                                     print("Here is a list of all your contacts")
#                                     print('\n')

#                                     for contact in display_contacts():
#                                             print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

#                                     print('\n')
#                             else:
#                                     print('\n')
#                                     print("You dont seem to have any contacts saved yet")
#                                     print('\n')

#                     elif short_code == 'fc':

#                             print("Enter the number you want to search for")

#                             search_number = input()
#                             if check_existing_contacts(search_number):
#                                     search_contact = find_contact(search_number)
#                                     print(f"{search_contact.first_name} {search_contact.last_name}")
#                                     print('-' * 20)

#                                     print(f"Phone number.......{search_contact.phone_number}")
#                                     print(f"Email address.......{search_contact.email}")
#                             else:
#                                     print("That contact does not exist")

#                     elif short_code == "ex":
#                             print("Bye .......")
#                             break
#                     else:
#                             print("I really didn't get that. Please use the short codes")