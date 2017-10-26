import code
import unittest

class TestCode(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(code.return_zero(),0)
        # Handin 1
        self.assertTrue(code.return_zero() == 0)
    def test_double(self):
        self.assertEqual(code.double(2),4)
        self.assertEqual(code.double(4),8)
        self.assertEqual(code.double(0),0)
        self.assertEqual(code.double(-2),-4)
        #Handin 2
    def test_triple(self):
        self.assertEqual(code.triple(2),6)
        self.assertEqual(code.triple(3),9)
    def test_if1(self):
        self.assertEqual(code.if1(0),'zero')
        self.assertEqual(code.if1(1),'positive')
        self.assertEqual(code.if1(-1),'negative')
    def test_if2(self):
        self.assertEqual(code.if2(0),'zero')
        self.assertEqual(code.if2(1),'positive')
        self.assertEqual(code.if2(-1),'negative')

    def test_loop1(self):
        self.assertEqual(code.loop1(0),0)
        self.assertEqual(code.loop1(19),19)
    def test_loop_sum(self):
        self.assertEqual(code.loop_sum(0),0)
        self.assertEqual(code.loop_sum(1),1)
        self.assertEqual(code.loop_sum(2),3)
        self.assertEqual(code.loop_sum(100),5050)
    def test_myjoin(self):
        split1 = "1,2,3,4".split(',')
        self.assertEqual(code.myjoin(split1,","),"1,2,3,4")
        self.assertEqual(
            code.myjoin("Hello and goodbye".split("and"),"and"),
            "Hello and goodbye")
        self.assertEqual(code.myjoin(['1'],','),'1')
if __name__ == '__main__':
    unittest.main()
