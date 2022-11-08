import os
import numpy

base_order = "jupyter nbconvert --to=Markdown "
path = r'/Users/zackyule/codeLearning/MyPythonCookBook/utils'
filenames = os.listdir(path)

for filename in filenames:
    print(filename)
    out_file_name = 'mds'+ os.sep + filename.split('.')[0]

    #todo: 筛选ipynb文件
    order = base_order + 'utils'+ os.sep + filename + ' --output ' + '..' + os.sep + out_file_name
    files = os.popen(order).readlines()