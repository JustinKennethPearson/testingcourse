from __future__ import print_function
import unittest
from random import * 
import sys
def add(x,y):
    return x+y

class TestAddition(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(add(3,4),7)

def test_add_random_single():
    x = randint(-sys.maxsize,sys.maxsize)
    y = randint(-sys.maxsize,sys.maxsize)
    assert(add(x,y) == x+y)

def test_add_random(max_iterations):
    i = 0;
    while(i<max_iterations):
        test_add_random_single()
        i += 1
        sys.stdout.write('.')
    print("\nRan ",max_iterations," tests.")

    
if __name__ == '__main__':
    test_add_random(1000)
    unittest.main()

