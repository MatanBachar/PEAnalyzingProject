# Matan Bachar - Cynet Project

# Writer that get a PE, Hash object and answers-queue and write the answers into a file called result.*something*
# Writer classes will have to implement this interface

from abc import ABCMeta, abstractmethod


# Interface
class Writer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def launch(self, filepath, hash_func, answers_queue): pass
