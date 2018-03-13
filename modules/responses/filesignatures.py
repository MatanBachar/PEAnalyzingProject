# Matan Bachar - Cynet Project

# This class is responsible for answering the question:"How many signatures existing on the PE?"

import yara
from modules.responses import responser


class FileSignaturesResponse(responser.Responser):
    def __init__(self):
        self.signatures = 0

    def response(self, exe_file):
        # callback after module
        def __module_callback(data):
            self.signatures = data.get('number_of_sections')

        exe_file.seek(0)
        dat = exe_file.read()
        rules = yara.compile(source='import "pe" rule a { condition: false }') # dummy rule
        # after reading the data, call the module_callback function and extract the asked parameter about the PE
        rules.match(data=dat, modules_callback=__module_callback)
        return "There are {} signatures in this file".format(self.signatures)


if __name__ == "__main__":
    with open('bsplayer269.1079.exe', 'rb') as exe_file:
        responser = FileSignaturesResponse()
        print(responser.response(exe_file))