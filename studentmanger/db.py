# coding:utf-8
from collections import namedtuple
student = namedtuple('Student','id name sex age address compony')
path = 'db.txt'
def read_(PATH =path):
    result = {}
    with open(PATH) as f:
        for line in f:
            line = line.split()
            try:
                id = int(line[0])
            except:
                return result
            news = student(*line)
            result[id] = news
    return result


def save_(student, PATH = path):
    with open(PATH,'w') as f:
        for va in student.values():
            line = ' '.join(map(str, tuple(va)))
            f.write(line+'\n')