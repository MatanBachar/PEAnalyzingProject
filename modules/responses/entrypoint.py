# Matan Bachar - Cynet Project

# This response class responsible for returning the entry point address of a PE.
# For executable files, this is the starting address. For device drivers, this is the address of the
# initialization function. The entry point function is optional for DLLs.
# When no entry point is present, this member is zero.

import yara
from modules.responses import responser


class FileEntryPointResponse(responser.Responser):
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
        responser = FileEntryPointResponse()
        print(responser.response(exe_file))