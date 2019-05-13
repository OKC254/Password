import unittest
from  user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Oscar","Kiplimo","oscar@gmail.com",)
    def test1(self):
        self.assertEqual(self.new_user.f_name,"Oscar")
        self.assertEqual(self.new_user.m_name,"Kiplimo")
        self.assertEqual(self.new_user.e_mail,"oscar@gmail.com")
    def test_save_user(self):
        self.new_user.save_user()

    def tearDown(self):
        User.userlist = []
    def test_delete_user(self):
        self.new_user.save_user()
        test_data= User("ariana","gathoni","ariana@gmail.com")
        test_data.save_user()
        self.assertEqual(len(User.user_list),2)
    def test_display_user(self):
        self.assertEqual(User.display_users(),User.user_list)    
if __name__ == '__main__':
    unittest.main()