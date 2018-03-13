# Matan Bachar - Cynet Project

# This Hash reposible for SHA256 hashing

from hashes import hash
import hashlib


class SHA256Hash(hash.Hash):
    def __init__(self):
        self.hash_func = hashlib.sha256()

    def hash(self, filepath):
        buf_size = 65536  # lets read stuff in 64kb chunks!
        with open(filepath, 'rb') as exe_file:
            while True:
                data = exe_file.read(buf_size)
                if not data:
                    break
                self.hash_func.update(data)
        hashed = self.hash_func.hexdigest()
        return str(hashed)

if __name__ == "__main__":
    func = SHA256Hash()
    with open('bsplayer269.1079.exe', 'rb') as exe_file:
        print(func.hash(exe_file))