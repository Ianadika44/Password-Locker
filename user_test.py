# import unittest  # Importing the unittest module
# from user import User  # Importing the contact class


# class TestUser(unittest.TestCase):

#     '''
#     Test class that defines test cases for the contact class behaviours.

#     Args:
#         unittest.TestCase: TestCase class that helps in creating test cases
#     '''

#     def setUp(self):
#         '''
#         Set up method to run before each test cases.
#         '''
#         self.new_user = User(
#             "Ian", "Adika", "123ABC", "adika19ian@gmail.com")  # create contact object

#     def test_init(self):
#         '''
#         test_init test case to test if the object is initialized properly
#         '''

#         self.assertEqual(self.new_user.account_name, "Ian")
#         self.assertEqual(self.new_user.user_name, "Adika")
#         self.assertEqual(self.new_user.password, "123ABC")
#         self.assertEqual(self.new_user.email, "adika19ian@gmail.com")

#     def test_save_user(self):
#         '''
#         test_save_contact test case to test if the contact object is saved into
#          the contact list
#         '''
#         self.new_user.save_user()  # saving the new contact
#         self.assertEqual(len(User.user_list), 1)

#     def tearDown(self):
#         '''
#         tearDown method that does clean up after each test case has run.
#         '''
#         User.user_list = []

#     def test_save_multiple_users(self):
#         '''
#         test_save_multiple_contact to check if we can save multiple contact
#         objects to our contact_list
#         '''
#         self.new_user.save_user()
#         test_user = User("Test", "user", "123ABC",
#                                      "adika19ian@gmail.com")  # new contact
#         test_user.save_user()
#         self.assertEqual(len(User.user_list), 2)

#     def test_delete_user(self):
#         '''
#         test_delete_contact to test if we can remove a contact from our contact list
#         '''
#         self.new_user.save_user()
#         test_user = User(
#             "Test", "user", "123ABC", "adika19ian@gmail.com")  # new contact
#         test_user.save_user()

#         self.new_user.delete_user()  # Deleting a contact object
#         self.assertEqual(len(User.user_list), 1)

#     def test_find_user_by_name(self):
#         '''
#         test to check if we can find a contact by phone number and display information
#         '''

#         self.new_user.save_user()
#         test_user = User(
#             "Test", "user", "123ABC", "adika19ian@gmail.com")  # new contact
#         test_user.save_user()

#         found_user = User.find_by_name("user")

#         self.assertEqual(found_user.email, test_user.email)

#     def test_user_exists(self):
#         '''
#         test to check if we can return a Boolean  if we cannot find the contact.
#         '''

#         self.new_user.save_user()
#         test_user = User(
#             "Test", "user", "123ABC", "adika19ian@gmail.com")  # new contact
#         test_user.save_user()

#         user_exists = User.user_exist("123ABC")

#         self.assertTrue(user_exists)

#     def test_display_all_users(self):
#         '''
#         method that returns a list of all contacts saved
#         '''

#         self.assertEqual(User.display_user(),
#                         User.user_list)
# if __name__ == '__main__':
#     unittest.main()
