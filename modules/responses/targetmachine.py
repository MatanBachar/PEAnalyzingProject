# Matan Bachar - Cynet Project

# This class is responsible for answering the question:"What is the target architecture of the PE?"

import yara
from modules.responses import responser


class FileTargetMachineResponse(responser.Responser):
    def __init__(self):
        self.TargetMachine = 0
        # Loading all possible values of the variable: 'machine' in YARA
        self.dictionary = {0: 'MACHINE_UNKNOWN', 1: 'MACHINE_AM33', 2: 'MACHINE_AMD64',
                           3: 'MACHINE_ARM', 4: 'MACHINE_ARMNT', 5: 'MACHINE_ARM64',
                           6: 'MACHINE_EBC', 7: 'MACHINE_I386', 8: 'MACHINE_IA64',
                           9: 'MACHINE_M32R', 10: 'MACHINE_MIPS16', 11: 'MACHINE_MIPSFPU',
                           12: 'MACHINE_MIPSFPU16', 13: 'MACHINE_POWERPC', 14: 'MACHINE_POWERPCFP',
                           15: 'MACHINE_R4000', 16: 'MACHINE_SH3', 17: 'MACHINE_SH3DSP',
                           18: 'MACHINE_SH4', 19: 'MACHINE_SH5', 20: 'MACHINE_THUMB',
                           21: 'MACHINE_WCEMIPSV2'}

    def response(self, exe_file):
        # callback after module
        def __module_callback(data):
            self.TargetMachine = data.get('machine')

        exe_file.seek(0)
        dat = exe_file.read()
        rules = yara.compile(source='import "pe" rule a { condition: false }')  # dummy rule
        # after reading the data, call the module_callback function and extract the asked parameter about the PE
        rules.match(data=dat, modules_callback=__module_callback)
        return "The target machine of the file is {}".format(self.dictionary[self.TargetMachine])


if __name__ == "__main__":
    with open('bsplayer269.1079.exe', 'rb') as exe_file:
        responser = FileTargetMachineResponse()
        print(responser.response(exe_file))
