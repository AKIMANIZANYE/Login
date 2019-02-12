import unittest
from sigin import User

class testing (unittest.TestCase):
    def setting(self):
        self.newuser= User("Claudine","111")
    def test_init(self):
        self.assertEqual(len(self.newuser.username,claudine)
        self.assertEqual(len(self.newuser.password,111)
    
    def saving (self):
        self.newuser.saving() 
        self.assertEqual(len(User.user_list),1)
   

    def delete(self):
         User.user_list.remove(self)
            
# def test_user_exists(self):


    self.newuser.saving()
    test_user = User("claudine","111")
    test_user.saving()
        self.newuser.delete

        self.assertTrue(User.user_list),1)

    
    def display(self):
    self.assertEqual(User.display(),User.user_list)   
  
    if __name__ ==  '__main__':
    unittest.main()
