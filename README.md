# baseX-py

Simple Python module, that can:

*   Encode any decimal number to its Base-X representation
*   Decode any Base-X number its decimal representation

X is anything from 2 to 62.

The alphabet used is ``012..789.9abc...xyzABC...XYZ``
            
## How to use

    from baseX.x import BaseX

    BaseX.encode(100, 2, min_len=5)
    BaseX.decode('0100', 2)

## Test suite

Can be ran using ``python setup.py test``
