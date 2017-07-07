# -*- coding: utf-8 -*-

try:
    from . import pySRE
except ImportError as e:
    print('%s: %s' % (e.name, e.msg))

class Metadata:
    def __init__(self):
        self.__version__ = '0.1.6'
        self.__author__ = 'Rubén de Celis Hernández'

    def get_version(self):
        return self.__version__
    def get_author(self):
        return self.__author__