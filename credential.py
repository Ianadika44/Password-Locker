import pyperclip
class Credential:
    """
    Class that generates new instances of credentials.
    """

    credential_list = []  # Empty contact list

    def __init__(self, credential_name, user_name, password, email):

      # docstring removed for simplicity

        self.credential_name = credential_name
        self.user_name = user_name
        self.password = password
        self.email = email

        # Init method up here
    def save_credential(self):
        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_name(cls, name):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for credential in cls.credential_list:
            if credential.credential_name == name:
                return credential

    @classmethod
    def credential_exist(cls, name):
        '''
          Method that checks if a contact exists from the contact list.
        Args:
              number: Phone number to search if it exists
        Returns :
              Boolean: True or false depending if the contact exists
        '''
        for credential in cls.credential_list:
            if credential.password == name:
                return True

            return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the contact list
        '''
        return cls.credential_list
    
    # @classmethod
    # def copy_email(cls,name):
    #     credential_found = Credential.find_by_name(name)
    #     pyperclip.copy(credential_found.email)
   