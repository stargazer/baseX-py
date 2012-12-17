import string             

class BaseX:
    """
    These 2 class methods, are used to convert decimal number to Base-X, and
    Base-X numbers, to decimal.

    Can be used for convertions of base-2 (binary), to base-64.
    """
    # ALPHABET = 0123...9abc..zABC...Z
    # They correspond to decimal digits 0-61
    ALPHABET = string.digits + string.ascii_letters
    
    # Minimum length of encoded numbers. If a number has less digits than this,
    # then it is padded with 0s.
    MIN_LEN = 1

    @classmethod
    def encode(cls, num, base):
        """
        Encode a decimal number in Base-X

        @param num : The number to encode
        @param base: The base to which to convert the number

        @return   : Number in Base62 encoding
        @rvalue   : str
        """
        if base < 2 or base > 62:
            raise ValueError('Illegal base')            

        if num == 0:
            return cls.ALPHABET[0]

        arr = []
        while num:
            rem = num % base
            num = num // base
            arr.append(cls.ALPHABET[rem])
        arr.reverse()

        # Pad with zeros in-front if needed 
        if len(arr) < cls.MIN_LEN:
            rem = cls.MIN_LEN - len(arr)
            for i in range(rem):
                arr.insert(0, '0')

        return ''.join(arr)

    @classmethod
    def decode(cls, string, base):
        """
        Decode a Base X encoded string into a decimal number

        @param string: The encoded number, in str format
        @param base:   The base from which to convert the number

        @return : Number in decimal encoding
        @rvalue : int
        """
        if base < 2 or base > 62:
            raise ValueError('Illegal base')            

        num = 0

        # If ``string`` is padded with zeros, remove them
        while 1:
            if string != '0' and string.startswith('0'):
                string = string[1:]
            else:
                break
        
        for power, char in enumerate(string[::-1]):
            try:
                index = cls.ALPHABET.index(char)
            except ValueError:
                # ``char`` is not contained in the alphabet
                raise ValueError('Number contains illegal digits')

            if index >= base:
                raise ValueError('Number contains illegal digits')

            num += index * (base ** power)

        return num
 
