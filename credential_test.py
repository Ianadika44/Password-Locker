import unittest  # Importing the unittest module
from credential import Credential  # Importing the contact class
# import pyperclip

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

#     def setUp(self):
#         '''
#         Set up method to run before each test cases.
#         '''
#         self.new_credential = Credential(
#             "Ian", "Adika", "123ABC", "adika19ian@gmail.com")  # create contact object

#     def test_init(self):
#         '''
#         test_init test case to test if the object is initialized properly
#         '''

#         self.assertEqual(self.new_credential.credential_name, "Ian")
#         self.assertEqual(self.new_credential.user_name, "Adika")
#         self.assertEqual(self.new_credential.password, "123ABC")
#         self.assertEqual(self.new_credential.email, "adika19ian@gmail.com")

#     def test_save_credential(self):
#         '''
#         test_save_contact test case to test if the contact object is saved into
#          the contact list
#         '''
#         self.new_credential.save_credential()  # saving the new contact
#         self.assertEqual(len(Credential.credential_list), 1)

#     def tearDown(self):
#         '''
#         tearDown method that does clean up after each test case has run.
#         '''
#         Credential.credential_list = []

#     def test_save_multiple_credential(self):
#         '''
#         test_save_multiple_contact to check if we can save multiple contact
#         objects to our contact_list
#         '''
#         self.new_credential.save_credential()
#         test_credential = Credential("Test", "user", "123ABC",
#                                      "adika19ian@gmail.com")  # new contact
#         test_credential.save_credential()
#         self.assertEqual(len(Credential.credential_list), 2)

#     def test_delete_credential(self):
#         '''
#         test_delete_contact to test if we can remove a contact from our contact list
#         '''
#         self.new_credential.save_credential()
#         test_credential = Credential(
#             "Test", "user", "123ABC", "adika19ian@gmail.com")  # new contact
#         test_credential.save_credential()

#         self.new_credential.delete_credential()  # Deleting a contact object
#         self.assertEqual(len(Credential.credential_list), 1)

#     def test_find_credential_by_name(self):
#         '''
#         test to check if we can find a contact by phone number and display information
#         '''

#         self.new_credential.save_credential()
#         test_credential = Credential(
#             "Test", "user", "123ABC", "adika19ian@gmail.com")  # new contact
#         test_credential.save_credential()

#         found_credential = Credential.find_by_name("Test")

#         self.assertEqual(found_credential.email, test_credential.email)

#     def test_credential_exists(self):
#         '''
#         test to check if we can return a Boolean  if we cannot find the contact.
#         '''

#         self.new_credential.save_credential()
#         test_credential = Credential(
#             "Test", "user", "123ABC", "adika19ian@gmail.com")  # new contact
#         test_credential.save_credential()

#         credential_exists = Credential.credential_exist("123ABC")

#         self.assertTrue(credential_exists)

#     def test_display_all_credentials(self):
#         '''
#         method that returns a list of all contacts saved
#         '''

#         self.assertEqual(Credential.display_credentials(),
#                          Credential.credential_list)

#     # def test_copy_email(self):
#     #     '''
#     #     Test to confirm that we are copying the email address from a found contact
#     #     '''

#     #     self.new_credential.save_credential()
#     #     Credential.copy_email("email")

#     #     self.assertEqual(self.new_credential.email, pyperclip.paste())
    

# if __name__ == '__main__':
#     unittest.main()
