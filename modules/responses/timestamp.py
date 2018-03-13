# Matan Bachar - Cynet Project

# This class is responsible for getting the timestamp of a file (and convert it).

import yara
import datetime

from modules.responses import responser


class TimestampResponse(responser.Responser):
    def __init__(self):
        self.timestamp = 0

    def response(self, exe_file):
        # callback after module
        def __module_callback(data):
            self.timestamp = data.get('timestamp')

        exe_file.seek(0)
        dat = exe_file.read()
        rules = yara.compile(source='import "pe" rule a { condition: false }') # dummy rule
        # after reading the data, call the module_callback function and extract the asked parameter about the PE
        rules.match(data=dat, modules_callback=__module_callback)
        # converting the Epoch timestamp using datetime class's method
        return "The compliation date (timestamp) of the file is at {}".format(
            datetime.datetime.fromtimestamp(int(self.timestamp)).strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    with open('bsplayer269.1079.exe', 'rb') as fh:
        responser = TimestampResponse()
        print(responser.response(fh))