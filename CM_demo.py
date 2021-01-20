
# from contextlib import contextmanager

# # class Open_file():
# #     """docstring for Open_file"""
# #     def __init__(self, filename, mode):
# #         self.filename = filename
# #         self.mode = mode

# #     def __enter__(self):
# #         self.file = open(self.filename, self.mode)
# #         return self.file

# #     def __exit__(self, exc_type, exc_val, traceback):
# #         self.file.close()
# #-------------------- OR------------------------

# @contextmanager
# def Open_file(file, mode):
#     f = open(file, mode)
#     yield f
#     f.close()

# with Open_file('sample.txt', 'w') as f:
#     f.write('lorem impsummm..yash testing')

# print(f.closed)

import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())
