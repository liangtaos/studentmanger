# coding:utf-8
from manger import Studentmanger
import log
import logging
logger = logging.getLogger(__name__)
class Studentuser(object):
    stud_m = Studentmanger()
    def __init__(self):
        pass

    def create(self):
        data = raw_input('请输入学生的信息;(姓名 性别 年龄 地址 公司ps用空格分割) : ').strip()
        if not len(data.split(' ')) == 5:
            print '输入信息格式错误，请重新输入'
            self.create()
        result = self.stud_m.create(data)
        print result.name,result.sex,result.age,result.address,result.compony

    def delete(self,id=None):
        if id == None:
            id = int(raw_input('请输入要删除学生的学号: '))

        con = self.stud_m.delete(id)
        if con:
            print '已经删除',con.name,con.address
        else:
            print '没有此学号'

    def update(self, id=None):
        if id == None:
             id = int(raw_input('请输入要更新学生的学号: '))
        data = raw_input('请输入学生的信息;(姓名 性别 年龄 地址 公司ps用空格分割) : ')
        if not len(data.split(' ')) == 5:
            print '输入信息格式错误，请重新输入'
            self.update()
        con = self.stud_m.update(id,data)
        if con:
           print '更新成功',con.name,con.sex,con.age,con.address
        else:
            print '该学号的学生不存在'

    def search(self, id=None):
        if id == None:
            id = int(raw_input('请输入要查询学生的学号: '))
        conn = self.stud_m.search(id)
        if conn:
            print conn.name,conn.age,conn.sex,conn.address,conn.compony
        else:
            print '不好意思没有你要查询的学号的学生'

    def exit(self):
        return


def main():
    stu = Studentuser()
    jieko = {'create': stu.create, 'delete': stu.delete, 'update': stu.update, 'search': stu.search, 'exit': stu.exit}
    try:
        caozuo = raw_input('请输入操作(create/delete/update/search/exit):')
        logger.info('命令[%s]' % caozuo)
        jieko[caozuo]()
    except:

        print '输入erroe'
        main()





if __name__ == '__main__':
    main()