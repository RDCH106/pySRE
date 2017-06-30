# pySRE

[![PyPI](https://img.shields.io/pypi/v/pySRE.svg)](https://pypi.python.org/pypi/pySRE)
[![PyPI](https://img.shields.io/pypi/pyversions/pySRE.svg)](https://pypi.python.org/pypi/pySRE)
[![PyPI](https://img.shields.io/pypi/l/pySRE.svg)](https://github.com/RDCH106/pySRE/blob/master/LICENSE)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3c484020aae54e939eb6624087ccfd27)](https://www.codacy.com/app/RDCH106/pySRE?utm_source=github.com&utm_medium=referral&utm_content=RDCH106/pySRE&utm_campaign=badger)

Experimental Python wrapper for **Simple-RFC1738-Encoder** written in JavasScript.

More info about Simple-RFC1738-Encoder: https://github.com/RDCH106/Simple-RFC1738-Encoder

### What can I do with Linearizator?

- The same as original library of Simple-RFC1738-Encoder

### Installation

You can install or upgrade pySRE with:

`$ pip install pySRE --upgrade`

Or you can install from source with:

```
$ git clone https://github.com/RDCH106/pySRE.git --recursive
$ cd pySRE
$ pip install -r requirements.txt
```

### Quick example

```python
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

```
