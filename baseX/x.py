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
    def encode(cls, num, base, min_len=1):
        """
        Encode a decimal number in Base-X

        @param num      : The number to encode
        @param base     : The base to which to convert the number
        @param min_len  : The minimum length(in digits) that the encoded number should
            have. For example, if we want that all our encoded numbers have at
            least 5 characters, any numbers that are smaller in length, will be
            padded with 0s in the front.

        @return   : Number in Base62 encoding
        @rvalue   : str
        """
        if base < 2 or base > 62:
            raise ValueError('Illegal base')            

        arr = []
        while num:
            rem = num % base
            num = num // base
            arr.append(cls.ALPHABET[rem])
        arr.reverse()

        # Pad with zeros in-front if needed 
        if len(arr) < min_len:

            rem = min_len - len(arr)
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
 
