class User:
    """
    Class that generates new instances of credentials.
    """

    user_list = []  # Empty contact list


    def __init__(self, account_name, user_name, password, email):

      # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.email = email

        # Init method up here
    def save_user(self):
        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_name(cls, name):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.user_list:
            if user.user_name == name:
                return user

    @classmethod
    def user_exist(cls, name):
        '''
          Method that checks if a contact exists from the contact list.
        Args:
              number: Phone number to search if it exists
        Returns :
              Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:
            if user.password == name:
                return True

            return False

    @classmethod
    def display_user(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list
    
   