'''
Created on 10 mag 2017

@author: Enrico
'''
import unittest
from calcolatrice import calcolatrice

class Test(unittest.TestCase):

    c = calcolatrice()


    def testName(self):
        self.assertTrue(self.c.dividi(100, 10))
        self.assertEqual(2+2, self.c.somma(2, 2))
        self.assertFalse(self.c.dividi(100, 10)==15)
        self.assertEqual(self.c.potenza(10, 2), 100)
        self.assertLess(10, self.c.moltiplica(5, 5))
        self.assertNotEqual(0, self.c.modulo(10, 7))
        self.assertGreaterEqual(self.c.somma(10, 10), self.c.somma(10, 9))
        self.assertGreater(self.c.differenza(11, 10), 10-10)
        self.assertIs(10, 10)
        
        self.failIfEqual(self.c.somma(10, 10), self.c.moltiplica(2, 20))
        self.failUnless(self.c.differenza(50, 10), 40)
        self.failIfAlmostEqual(self.c.differenza(5, 5), 5+6)
        self.failUnlessEqual(self.c.moltiplica(2, 2), self.c.somma(2, 2))
        self.failIf(self.c.moltiplica(10, 3)==31)
        
        self.assertEqual(self.c.intToBit(1), 1)


