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
        delete_credential method deletes a saved contact from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_name(cls, name):
        '''
        Method that takes in a user name and returns a credential that matches that name.

        Args:
            name: user name to search for
        Returns :
            Contact of person that matches the number.
        '''

        for credential in cls.credential_list:
            if credential.credential_name == name:
                return credential

    @classmethod
    def credential_exist(cls, name):
        '''
          Method that checks if a credential exists from the credential list.
        Args:
              name: user to search if it exists
        Returns :
              Boolean: True or false depending if the user exists
        '''
        for credential in cls.credential_list:
            if credential.password == name:
                return True

            return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
