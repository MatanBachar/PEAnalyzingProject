import sys
import threading
import queue
import hashes.sha256_hash
from writers import csv_writer
from modules.analyzers import common_analyzer
from modules.answer_producers import common_answer_producer


def main():

    filepath = sys.argv[1]
    question_file_path = sys.argv[2]
    answers_queue = queue.Queue()
    question_analyzer = common_analyzer.CommonAnalyzer()
    answer_producer = common_answer_producer.CommonAnswerProducer(filepath, question_file_path, answers_queue
                                                                  , question_analyzer)
    result_writer = csv_writer.CSVWriter()
    sha256 = hashes.sha256_hash.SHA256Hash()

    answer_thread = threading.Thread(target=answer_producer.launch())
    writer_thread = threading.Thread(target=result_writer.launch(filepath, sha256, answers_queue))
    answer_thread.start()
    writer_thread.start()


if __name__ == "__main__":
    main()



