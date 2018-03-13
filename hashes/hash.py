# Matan Bachar - Cynet Project

# Hash classes that responsible for hashing files for the result.csv file will implement this interface

from abc import ABCMeta, abstractmethod


# Interface
class Hash(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def hash(self, filepath): pass
