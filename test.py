import unittest
from sigin import User

class testing (unittest.TestCase):
    def setUp(self):
        self.newuser= User("Claudine","111")
    def test_init(self):
        self.assertEqual(self.newuser.username,"Claudine")
        self.assertEqual(self.newuser.password,"111")
    
    def saving (self):
        self.newuser.saving() 
        self.assertEqual(len(User.user_list),1)
   

    def test_delete(self):
       User.user_list.remove(self)
            
        
# def test_user_exists(self):


        self.newuser.saving()
        test_user = User("claudine","111")
        test_user.saving()
        self.newuser.delete()

        self.assertTrue(len(User.user_list),1)

    
    def test_display(self):
        self.newuser.saving()
        test_user = User("claudine","111")
        test_user.saving()
        self.assertTrue(len(User.user_list),2)   
  
if __name__ ==  '__main__':
    unittest.main()
