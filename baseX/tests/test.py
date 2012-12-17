from unittest import TestCase
from baseX.x import BaseX

class TestInvalidBase(TestCase):
    """
    In this testclass, we run the class methods, providing illegal values for
    the ``base`` parameter.
    """
    def test_encode(self):        
        # Give base=0. Should raise ValueError
        self.assertRaises(
            ValueError,
            BaseX.encode,
            100, 0,            
        )
        # Give base=1. Should raise ValueError
        self.assertRaises(
            ValueError,
            BaseX.encode,
            100, 1,            
        )
        # Give base=63. Should raise ValueError
        self.assertRaises(
            ValueError,
            BaseX.encode,
            100, 63,            
        )

    def test_decode(self):
        # Give base=0. Should raise ValueError
        self.assertRaises(
            ValueError,
            BaseX.decode,
            '100', 0,            
        )
        # Give base=1. Should raise ValueError
        self.assertRaises(
            ValueError,
            BaseX.decode,
            '100', 1,            
        )
        # Give base=63. Should raise ValueError
        self.assertRaises(
            ValueError,
            BaseX.decode,
            '100', 63,            
        )


class TestBase2(TestCase):
    """
    In this class, we check the outputs of the class methods, 
    for Base-2 (binary) conversions.
    """                                                         
    BASE = 2

    def test_encode(self):
        self.assertEqual(BaseX.encode(0, self.BASE), '0')
        self.assertEqual(BaseX.encode(0, self.BASE, 3), '000')

        self.assertEqual(BaseX.encode(1, self.BASE), '1')
        self.assertEqual(BaseX.encode(1, self.BASE, 5), '00001')

        self.assertEqual(BaseX.encode(2, self.BASE), '10')
        self.assertEqual(BaseX.encode(2, self.BASE, 4), '0010')

        self.assertEqual(BaseX.encode(100, self.BASE), '1100100')
        self.assertEqual(BaseX.encode(100, self.BASE, 10), '0001100100')

        self.assertEqual(BaseX.encode(512, self.BASE), '1000000000')
        self.assertEqual(BaseX.encode(512, self.BASE, 5), '1000000000')

        self.assertEqual(BaseX.encode(1070080, self.BASE), '100000101010000000000')
        self.assertEqual(BaseX.encode(1070080, self.BASE, 10), '100000101010000000000')

        self.assertEqual(BaseX.encode(9598070080, self.BASE), '1000111100000101101110110101000000')
        self.assertEqual(BaseX.encode(9598070080, self.BASE, 8), '1000111100000101101110110101000000')
                    
    def test_decode(self):
        self.assertEqual(BaseX.decode('0', self.BASE), 0)
        self.assertEqual(BaseX.decode('0000', self.BASE), 0)
        
        self.assertEqual(BaseX.decode('1', self.BASE), 1)
        self.assertEqual(BaseX.decode('0001', self.BASE), 1)

        self.assertEqual(BaseX.decode('10', self.BASE), 2)
        self.assertEqual(BaseX.decode('00010', self.BASE), 2)

        self.assertEqual(BaseX.decode('1100100', self.BASE), 100)
        self.assertEqual(BaseX.decode('0001100100', self.BASE), 100)

        self.assertEqual(BaseX.decode('1000000000', self.BASE), 512)
        self.assertEqual(BaseX.decode('0001000000000', self.BASE), 512)

        self.assertEqual(BaseX.decode('100000101010000000000', self.BASE), 1070080)
        self.assertEqual(BaseX.decode('000100000101010000000000', self.BASE), 1070080)

        self.assertEqual(BaseX.decode('1000111100000101101110110101000000', self.BASE),9598070080)
        self.assertEqual(BaseX.decode('0001000111100000101101110110101000000', self.BASE), 9598070080)

        
        # Number contains a chat not included in our alphabet
        self.assertRaises(
            ValueError,
            BaseX.decode,
            '1#0', self.BASE
        )

        # Number contains a char not compatible with binary
        self.assertRaises(
            ValueError,
            BaseX.decode,
            '150', self.BASE
        )


class TestBase62(TestCase):
    """
    In this class, we check the outputs of the class methods, 
    for Base-2 (binary) conversions.
    """                                                         
    BASE = 62

    def test_encode(self):
        self.assertEqual(BaseX.encode(0, self.BASE), '0')
        self.assertEqual(BaseX.encode(0, self.BASE, 5), '00000')

        self.assertEqual(BaseX.encode(1, self.BASE), '1')
        self.assertEqual(BaseX.encode(1, self.BASE, 3), '001')
        
        self.assertEqual(BaseX.encode(2, self.BASE), '2')
        self.assertEqual(BaseX.encode(2, self.BASE, 5), '00002')

        self.assertEqual(BaseX.encode(100, self.BASE), '1C')
        self.assertEqual(BaseX.encode(100, self.BASE, 4), '001C')

        self.assertEqual(BaseX.encode(512, self.BASE), '8g')
        self.assertEqual(BaseX.encode(512, self.BASE, 3), '08g')

        self.assertEqual(BaseX.encode(1070080, self.BASE), '4unm')
        self.assertEqual(BaseX.encode(1070080, self.BASE, 10), '0000004unm')

        self.assertEqual(BaseX.encode(9598070080, self.BASE), 'atywtW')
        self.assertEqual(BaseX.encode(9598070080, self.BASE, 3), 'atywtW')
                    
    def test_decode(self):
        self.assertEqual(BaseX.decode('0', self.BASE), 0)
        self.assertEqual(BaseX.decode('0000', self.BASE), 0)
        
        self.assertEqual(BaseX.decode('1', self.BASE), 1)
        self.assertEqual(BaseX.decode('0001', self.BASE), 1)

        self.assertEqual(BaseX.decode('2', self.BASE), 2)
        self.assertEqual(BaseX.decode('0002', self.BASE), 2)

        self.assertEqual(BaseX.decode('1C', self.BASE), 100)
        self.assertEqual(BaseX.decode('0001C', self.BASE), 100)

        self.assertEqual(BaseX.decode('8g', self.BASE), 512)
        self.assertEqual(BaseX.decode('0008g', self.BASE), 512)

        self.assertEqual(BaseX.decode('4unm', self.BASE), 1070080)
        self.assertEqual(BaseX.decode('0004unm', self.BASE), 1070080)

        self.assertEqual(BaseX.decode('atywtW', self.BASE), 9598070080)
        self.assertEqual(BaseX.decode('000atywtW', self.BASE), 9598070080)

        # Number contains a chat not included in our alphabet
        self.assertRaises(
            ValueError,
            BaseX.decode,
            '1#0', self.BASE
        )


