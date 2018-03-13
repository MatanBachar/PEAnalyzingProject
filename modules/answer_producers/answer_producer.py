# Matan Bachar - Cynet Project

# AnswerProducer that gets PE, questions, answers-queue and analyzer. Answers the question using the analyzer and put
#  them into the queue.

from abc import ABCMeta, abstractmethod


class AnswerProducer(object):
    __metaclass__ = ABCMeta

    def __init__(self, exe_file_name, question_file_name, answers_queue, analyzer):
        self.exe_file_name = exe_file_name
        self.question_file_name = question_file_name
        self.answers_queue = answers_queue
        self.analyzer = analyzer


    @abstractmethod
    def launch(self): pass
