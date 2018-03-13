# Matan Bachar - Cynet Project

# This AnswerProducer get questions by file analyze them and then put them into queue

from modules.answer_producers import answer_producer


class CommonAnswerProducer(answer_producer.AnswerProducer):
    def __init__(self, exe_file_name, question_file_name, answers_queue, analyzer):
        super().__init__(exe_file_name, question_file_name, answers_queue, analyzer)

    def launch(self):
        with open(self.question_file_name) as questions_file:
            question = questions_file.readline()
            with open(self.exe_file_name, 'rb') as exe_file:
                # while there are still questions on the file
                while question:
                    analyzed = self.analyzer.analyze(question)
                    if analyzed:
                        answer = analyzed.response(exe_file)
                        self.answers_queue.put(answer)
                    elif question == '\n': pass
                    else:
                        self.answers_queue.put("Unrecognized question")
                    question = questions_file.readline()
        # symbolize for writer that there are know more answers coming
        self.answers_queue.put("END")