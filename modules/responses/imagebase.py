# Matan Bachar - Cynet Project

# This response class responsible for returning the image base address of a PE.
# The image base address is the address where windows will try to place the PE (if that If that does not succeed, that
# is if the given address range is already reserved by another PE, the PE is relocated
# to an address determined at runtime by Windows.

import yara
from modules.responses import responser



class FileImageBaseResponse(responser.Responser):
    def __init__(self):
        self.image_base = 0

    def response(self, exe_file):
        # callback after module
        def __module_callback(data):
            self.image_base = data.get('image_base')

        exe_file.seek(0)
        dat = exe_file.read()
        rules = yara.compile(source='import "pe" rule a { condition: false }') # dummy rule
        # after reading the data, call the module_callback function and extract the asked parameter about the PE
        rules.match(data=dat, modules_callback=__module_callback)
        return "The image base address is {}".format(self.image_base)


if __name__ == "__main__":
    with open('bsplayer269.1079.exe', 'rb') as exe_file:
        responser = FileImageBaseResponse()
        print(responser.response(exe_file))