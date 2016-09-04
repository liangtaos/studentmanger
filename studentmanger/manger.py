# coding:utf-8
from collections import namedtuple
from db import read_, save_,student


def get_id(keys,max_id):
    for i in range(1, max_id):
        if i in keys:
            continue
        else:
            new_id = i
            return new_id
    return None
class Studentmanger(object):
    def __init__(self):
        pass

    def create(self, data):
        data_list = data.split()
        result = read_()
        if not result:
            new_id = 1
        else:
            keys = result.keys()
            max_id =  max(keys)
            new_id = get_id(keys,max_id)
            if  not new_id:
                new_id = max_id + 1
        data_list.insert(0, new_id)
        #print data_list
        news = student(*data_list)
        result[new_id] = news
        save_(result)
        return result[new_id]

    def delete(self, id):
        result = read_()
        if not id in result.keys():
            return False
        data = result[id]
        result.pop(id)
        save_(result)
        return data

    def update(self, id,data):
        result = read_()
        if not id in result.keys():
            return False
        result.pop(id)
        data = data.split()
        data.insert(0, id)
        news = student(*data)
        result[id] = news
        save_(result)
        return result[id]

    def search(self, id):
        result = read_()
        try:
            data = result[id]
        except:
            return False
        return data