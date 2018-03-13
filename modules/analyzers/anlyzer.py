# Matan Bachar - Cynet Project

# Analyzers classes that responsible for analyze question string will have to implement this interface

from abc import ABCMeta, abstractmethod


# Interface
class Analyzer(object):
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def analyze(question): pass




