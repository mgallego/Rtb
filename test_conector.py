import conector
import unittest
import oauth2

class TestConector(unittest.TestCase):
    
    def setUp(self):
        self.conector = conector.Conector();

    def testGetConexion(self):
        self.assertEqual(type(self.conector.getConexion()), oauth2.Client)


if __name__ == '__main__':
    unittest.main() 
