import toEnglish
import unittest

class TesttoEnglish(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(toEnglish.toEnglish(0),'zero')
        self.assertEqual(toEnglish.toEnglish(1),'one')
        self.assertEqual(toEnglish.toEnglish(2),'two')
        self.assertEqual(toEnglish.toEnglish(3),'three')
        self.assertEqual(toEnglish.toEnglish(4),'four')
        self.assertEqual(toEnglish.toEnglish(5),'five')
        self.assertEqual(toEnglish.toEnglish(6),'six')
        self.assertEqual(toEnglish.toEnglish(7),'seven')
        self.assertEqual(toEnglish.toEnglish(8),'eight')
        self.assertEqual(toEnglish.toEnglish(9),'nine')
        self.assertEqual(toEnglish.toEnglish(10),'ten')
        self.assertEqual(toEnglish.toEnglish(11),'eleven')
        self.assertEqual(toEnglish.toEnglish(12),'twelve')
        self.assertEqual(toEnglish.toEnglish(13),'thirteen')
        self.assertEqual(toEnglish.toEnglish(14),'fourteen')
        self.assertEqual(toEnglish.toEnglish(15),'fifteen')
        self.assertEqual(toEnglish.toEnglish(16),'sixteen')
        self.assertEqual(toEnglish.toEnglish(17),'seventeen')
        self.assertEqual(toEnglish.toEnglish(18),'eighteen')
        self.assertEqual(toEnglish.toEnglish(19),'nineteen')
        self.assertEqual(toEnglish.toEnglish(20),'twenty')
    def test_tens(self):
        self.assertEqual(toEnglish.toEnglish(21),'twenty one')
        self.assertEqual(toEnglish.toEnglish(22),'twenty two')
        self.assertEqual(toEnglish.toEnglish(23),'twenty three')
        self.assertEqual(toEnglish.toEnglish(29),'twenty nine')
        self.assertEqual(toEnglish.toEnglish(30),'thirty')
        self.assertEqual(toEnglish.toEnglish(31),'thirty one')
        self.assertEqual(toEnglish.toEnglish(32),'thirty two')
        self.assertEqual(toEnglish.toEnglish(39),'thirty nine')
        self.assertEqual(toEnglish.toEnglish(40),'forty')
        self.assertEqual(toEnglish.toEnglish(41),'forty one')
        self.assertEqual(toEnglish.toEnglish(49),'forty nine')
        self.assertEqual(toEnglish.toEnglish(50),'fifty')
        self.assertEqual(toEnglish.toEnglish(51),'fifty one')
        self.assertEqual(toEnglish.toEnglish(59),'fifty nine')
        self.assertEqual(toEnglish.toEnglish(60),'sixty')
        self.assertEqual(toEnglish.toEnglish(61),'sixty one')
        self.assertEqual(toEnglish.toEnglish(69),'sixty nine')
        self.assertEqual(toEnglish.toEnglish(70),'seventy')
        self.assertEqual(toEnglish.toEnglish(71),'seventy one')
        self.assertEqual(toEnglish.toEnglish(79),'seventy nine')
        self.assertEqual(toEnglish.toEnglish(80),'eighty')
        self.assertEqual(toEnglish.toEnglish(81),'eighty one')
        self.assertEqual(toEnglish.toEnglish(85),'eighty five')
        self.assertEqual(toEnglish.toEnglish(90),'ninety')
        self.assertEqual(toEnglish.toEnglish(91),'ninety one')
        self.assertEqual(toEnglish.toEnglish(99),'ninety nine')
    def test_hundreds(self):
        self.assertEqual(toEnglish.toEnglish(100),'one hundred')
        self.assertEqual(toEnglish.toEnglish(200),'two hundred')
        self.assertEqual(toEnglish.toEnglish(201),'two hundred and one')
        self.assertEqual(toEnglish.toEnglish(436),'four hundred and thirty six')
        self.assertEqual(toEnglish.toEnglish(999),'nine hundred and ninety nine')
        
        








if __name__ == '__main__':
    unittest.main()

