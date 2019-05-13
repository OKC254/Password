import unittest
from credentials import Info

class TestInfo(unittest.TestCase):
    def setUp(self):
        self.new_info =Info("oscar.kiplimo","kiplimo.oscar")
    def test_init(self):
        self.assertEqual(self.new_info.face_bookp,"oscar.kiplimo")
        self.assertEqual(self.new_info.email_p,"kiplimo.oscar")
    def test_save_info(self):
        '''
        to test if user info is saved
        '''
        self.new_info.save_info()
        self.assertEqual(len(Info.info_list),1)
    def tearDown(self):
        Info.info_list = []
    def test_delete_info(self):
        self.new_info.save_info()
        test_info = Info("agens.89","agnes.89")
        test_info.save_info()
        test_info.delete_info()
        self.assertEqual(len(Info.info_list),1)
    def test_display_creds(self):
        self.assertEqual(Info.display_info(),Info.info)

if __name__ == '__main__':
    unittest.main()
