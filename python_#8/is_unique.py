#is uinique : Implement an Algorithm to determine if a string has all uinique characters
import unittest

def unique(str):
    char_set={}
    for char in str:
       
        if char in char_set:
            return False
        char_set[char]=1
    return True
class Test(unittest.TestCase):
    dataT =[('abcd'), ('sd432wq'), ('')]
    dataF=[('wadas22'),('2qdasdas sd')]

    def test_unique(self):
        # true check
        for test_case in self.dataT:
            actualResult = unique(test_case)
            self.assertTrue(actualResult)
        #false check
        for test_case in self.dataF:
            actualResult = unique(test_case)
            self.assertFalse(actualResult)
if  __name__== "__main__":
   unittest.main()