# Matan Bachar - Cynet Project

# This class is responsible for answering the question: "What is the size of the PE?"

import os
from modules.responses import responser


class FileSizeResponse(responser.Responser):
    def response(self, exe_file):
        filesize = os.path.getsize(exe_file.name)
        i = 0
        while (filesize/1024) > 1:
            filesize /= 1024
            i += 1
        filesize = int(filesize)
        if i == 1:
            unit = "KB"
        elif i == 2:
            unit = "MB"
        elif i == 3:
            unit = "GB"
        elif i == 4:
            unit = "TB"
        elif i == 5:
            unit = "PB"
        else:
            i -= 5
            while i > 0:
                filesize *= 1024
                unit = "PB"
        return "The size of the file is {}{}".format(filesize, unit)


if __name__ == "__main__":
    with open('bsplayer269.1079.exe') as exe_file:
        obj = FileSizeResponse()
        print(obj.response(exe_file))
