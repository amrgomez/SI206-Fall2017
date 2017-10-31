import unittest
import re



def test_alpha(s):
    f = open('opinion.html','r')

    pattern ='[a-zA-Z]+'
    result = re.findall(pattern,s)
    print(result)

    if len(result) >= 1:
        return re.findall(pattern,s)
    return None


def find_comments(s):
    pattern ='/\*.*\*/'
    result = re.findall(pattern,s)
    print(result)
    
    if len(result) >= 1:
        return re.findall(pattern,s)
    return None


def check_zip(s):
    pattern ='^[0-9]{5}(?:-[0-9]{4})?$'
    result = re.match(pattern,s)
    return result


test_alpha('')

####### UNIT TESTING BELOW; DO NOT CHANGE ANY TESTING CODE #######

class Alpha(unittest.TestCase):
    def test_alpha1(self):
        self.assertEqual(test_alpha('a b de 23 r4'),['a','b', 'de', 'r'])
    def test_alpha2(self):
        self.assertEqual(test_alpha('abde23r4'),['abde', 'r'])
    def test_alpha2(self):
        self.assertNotEqual(test_alpha('abde23r4'),['a','b', 'd', 'e', 'r'])


class Comments(unittest.TestCase):
    def test_alpha1(self):
        self.assertEqual(test_alpha('a b de 23 r4'),['a','b', 'de', 'r'])
    def test_alpha2(self):
        self.assertEqual(test_alpha('abde23r4'),['abde', 'r'])
    def test_alpha2(self):
        self.assertNotEqual(test_alpha('abde23r4'),['a','b', 'd', 'e', 'r'])



class Zip(unittest.TestCase):
    def test_pcw_1(self):
        self.assertTrue(check_zip('48103'))
    def test_pcw_2(self):
        self.assertTrue(check_zip('48103-1234'))
    def test_pcw_3(self):
        self.assertFalse(check_zip('4810'))
    def test_pcw_4(self):
        self.assertFalse(check_zip('48103-'))
    def test_pcw_5(self):
        self.assertFalse(check_zip('48103-12'))



if __name__ == "__main__":
    unittest.main(verbosity=2)
