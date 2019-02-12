import unittest
import readfile

class ReadFiles(unittest.TestCase):
     with open("test.txt","r") as inter:
            data = inter.read()
            self.assertEqual(data,readfiles.read_file("test.txt")) 
if __name__ == "__main__":
    unittest.main()