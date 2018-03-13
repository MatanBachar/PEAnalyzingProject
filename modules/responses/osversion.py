# Matan Bachar - Cynet Project

# This class is responsible for answering the question:"What is the minimum required OS to run this PE?"

import yara
from modules.responses import responser


class FileRequiredOSResponse(responser.Responser):
    def __init__(self):
        self.required = 0
        # Loading all possible values of the variable: 'os_version' in YARA
        self.dictionary = {1.0: "Windows 1.01", 2.1: "Windows 2.10", 3.0: "Windows 3.0"
                           , 3.1: "Windows 3.1", 3.2: "Windows 3.2", 3.5: "Windows NT 3.5"
                           , 4.0: "Windows 95", 4.1: "Windows 98", 4.9: "Windows ME"
                           , 5.0: "Windows 2000", 5.1: "Windows XP", 5.2: "Windows XP Professional x64"
                           , 6.0: "Windows Vista", 6.1: "Windows 7", 6.2: "Windows 8"
                           , 6.3: "Windows 8.1", 10.0: "Windows 10"}

    def response(self, exe_file):
        # callback after module
        def __module_callback(data):
            self.required = data.get('os_version')

        exe_file.seek(0)
        dat = exe_file.read()
        rules = yara.compile(source='import "pe" rule a { condition: false }') # dummy rule
        # after reading the data, call the module_callback function and extract the asked parameter about the PE
        rules.match(data=dat, modules_callback=__module_callback)
        # 'required' is equals to{'minor': 'X', 'major': 'Y'} so after
        # taking the minor and the major we will need to reverse it and adding '.' between and then we're getting Y.X
        version = float((".".join(str(self.required)[10:23:12])[::-1]))
        return "The required OS for this file is {}".format(self.dictionary[version])


if __name__ == "__main__":
    with open('bsplayer269.1079.exe', 'rb') as exe_file:
        responser = FileRequiredOSResponse()
        print(responser.response(exe_file))