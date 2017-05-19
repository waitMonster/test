# -*- coding: utf-8 -*-
import os,sys
class Files:#该模块用于获取指定路径下的文件名，可为需要上传文件的接口提供相关数据
    def __init__(self):
        self.path = os.path.abspath('.')+'\\'
        self.names = []
        #print self.path
    def get_all_files(self,dir_name):
        try:
            path_name = self.path+dir_name
            for name1 in os.listdir(path_name):
                file_name1 = os.path.join(path_name,name1)
                if os.path.isdir(file_name1):
                    for name2 in os.listdir(file_name1):
                        file_name2 = os.path.join(file_name1,name2)
                        self.names.append(file_name2)
                else:
                    self.names.append(file_name1)
        except Exception,e:
            print u'目录不存在'+str(e)

        return self.names

if __name__ == '__main__':
    F = Files()
    print F.get_all_files('F_iles')
























