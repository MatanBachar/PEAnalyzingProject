# Matan Bachar - Cynet Project

# This class is writing the answers given from the queue into
# CSV file called "result.csv"


from writers import writer
import csv
import queue


class CSVWriter(writer.Writer):
    def launch(self, filepath, hash_func, answers_queue):
        answers = ""
        # while there are still answers coming, remove them from the queue and append them to the answers
        while True:
            answer = answers_queue.get()
            if answer == "END":
                break
            answers += answer
            answers += '\n'
        fieldnames = ['file_name', 'file_signature', 'answers']
        with open("result.csv", 'w') as result_file:
            csv_writer = csv.writer(result_file, delimiter=',')
            csv_writer.writerow([filepath, str(hash_func.hash(filepath)), answers])



