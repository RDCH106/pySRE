# -*- coding: utf-8 -*-

from pySRE import pySRE

# Choose your Engine using:
#    pySRE.SUPPORTED_ENGINES
#
# Example:
#    pySRE.PySRC(pySRE.SUPPORTED_ENGINES.Node)

pySRE = pySRE.PySRC()  # automatically picks the best runtime
print("\nCurrrent engine: %s\n" % pySRE.execjs_engine)

my_str = "Rubén de Celis Hernández"
print("Original string: %s" % my_str)
my_str = pySRE.utf8_encode(my_str)
print("UTF8 encoded string: %s" % my_str)
my_str = pySRE.utf8_decode(my_str)
print("UTF8 decoded string: %s" % my_str)
