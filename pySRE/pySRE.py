# -*- coding: utf-8 -*-

import execjs
import os

class PySRC:

    def __init__(self):

        self.master_file = ""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + "/Simple-RFC1738-Encoder/js/common.js") as f:
            file = f.read()
            self.master_file += file + "\n\n"

        with open(dir_path + "/Simple-RFC1738-Encoder/js/encode.js") as f:
            file = f.read()
            self.master_file += file + "\n\n"

        with open(dir_path + "/Simple-RFC1738-Encoder/js/decode.js") as f:
            file = f.read()
            self.master_file += file + "\n\n"

        with open(dir_path + "/Simple-RFC1738-Encoder/js/utf8.js") as f:
            file = f.read()
            self.master_file += file

            #print(self.master_file)

        self.ctx = execjs.compile(self.master_file)

    def convert_to_url(self, str):
        return self.ctx.call("encode", str)

    def convert_to_url_with_utf8(self, str):
        return self.ctx.call("encode", self.ctx.call("utf8_encode", str))

    def convert_to_string(self, url):
        return self.ctx.call("decode", url)

    def convert_to_string_with_utf8(self, url):
        return self.ctx.call("utf8_decode", self.ctx.call("decode", url))

    def utf8_encode(self, str):
        return self.ctx.call("utf8_encode", str)

    def utf8_decode(self, str):
        return self.ctx.call("utf8_decode", str)