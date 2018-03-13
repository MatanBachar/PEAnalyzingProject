# Matan Bachar - Cynet Project

# This class is responsible for answering the question:"What is the minimum subsystem to run this PE?"

import yara
from modules.responses import responser


class FileSubsystemResponse(responser.Responser):
    def __init__(self):
        self.subsystem = 0
        self.dictionary = {0: 'SUBSYSTEM_UNKNOWN', 1: 'SUBSYSTEM_NATIVE', 2: 'SUBSYSTEM_WINDOWS_GUI',
                           3: 'SUBSYSTEM_WINDOWS_CUI', 4: 'SUBSYSTEM_OS2_CUI', 5: 'SUBSYSTEM_POSIX_CUI',
                           6: 'SUBSYSTEM_NATIVE_WINDOWS'}

    def response(self, exe_file):
        # callback after module
        def __module_callback(data):
            self.subsystem = data.get('subsystem')

        exe_file.seek(0)
        dat = exe_file.read()
        rules = yara.compile(source='import "pe" rule a { condition: false }') # dummy rule
        # after reading the data, call the module_callback function and extract the asked parameter about the PE
        rules.match(data=dat, modules_callback=__module_callback)
        return "The subsystem of the file is {}".format(self.dictionary[self.subsystem])


if __name__ == "__main__":
    with open('bsplayer269.1079.exe', 'rb') as exe_file:
        responser = FileSubsystemResponse()
        print(responser.response(exe_file))
