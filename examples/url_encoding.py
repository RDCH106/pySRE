# -*- coding: utf-8 -*-

from pySRE import pySRE

# Choose your Engine using:
#    pySRE.SUPPORTED_ENGINES
#
# Example:
#    pySRE.PySRC(pySRE.SUPPORTED_ENGINES.Node)

pySRE = pySRE.PySRC()  # automatically picks the best runtime
print("\nCurrrent engine: %s\n" % pySRE.execjs_engine)

my_url = "http://mascandobits.es?fullname=Rubén de Celis Hernández"
print("Original URL: %s" % my_url)
my_url = pySRE.convert_to_url(my_url)
print("RFC1738 URL: %s" % my_url)
my_url = pySRE.convert_to_string(my_url)
print("Decoded RFC1738 URL: %s" % my_url)
my_url = pySRE.convert_to_url_with_utf8(my_url)
print("RFC1738 URL with UTF8: %s" % my_url)
my_url = pySRE.convert_to_string_with_utf8(my_url)
print("Decoded RFC1738 URL with UTF8: %s" % my_url)
