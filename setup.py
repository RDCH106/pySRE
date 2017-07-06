from setuptools import setup
from pySRE import Metadata

metadata = Metadata()

def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

long_description = """
Experimental Python wrapper for **Simple-RFC1738-Encoder** written in JavasScript.

More info about Simple-RFC1738-Encoder: https://github.com/RDCH106/Simple-RFC1738-Encoder

************************************
What can I do with pySRE?
************************************

- The same as original library of Simple-RFC1738-Encoder


Installation
============

You can install or upgrade pySRE with:

- ``$ pip install pySRE --upgrade``

Or you can install from source with:

- ``$ git clone https://github.com/RDCH106/pySRE.git --recursive``
- ``$ cd pySRE``
- ``$ pip install -r requirements.txt``


Quick example
=============

``---------------------------------``

.. code-block:: python

   from pySRE import pySRE

   # Choose your Engine using:
   #    pySRE.SUPPORTED_ENGINES
   #
   # Example:
   #    pySRE.PySRC(pySRE.SUPPORTED_ENGINES.Node)

   pySRE = pySRE.PySRC()  # automatically picks the best runtime
   print("\\nCurrrent engine: %s\\n" % pySRE.execjs_engine)

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
   """

setup(
    name = 'pySRE',
    packages = ['pySRE', ''],
    package_data={'pySRE': ['Simple-RFC1738-Encoder/*',
                            'Simple-RFC1738-Encoder/js/*.js',
                            'Simple-RFC1738-Encoder/css/*.css',
                            'Simple-RFC1738-Encoder/img/*'],
                  '': ['requirements.txt']},
    version = metadata.get_version(),
    install_requires=requirements(),
    license = 'GPL v3',
    description = 'Experimental Python wrapper for Simple-RFC1738-Encoder written in JavasScript.',
    long_description= long_description,
    author = metadata.get_author(),
    author_email = 'contact@rdch106.hol.es',
    url = 'https://github.com/RDCH106/pySRE',
    download_url = 'https://github.com/RDCH106/pySRE/archive/v'+metadata.get_version()+'.tar.gz',
    keywords = 'python-wrapper url-encoder javascript',
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)