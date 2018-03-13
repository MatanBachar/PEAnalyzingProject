from abc import ABCMeta, abstractmethod


# Interface
class Responser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def response(self, exe_file): pass
