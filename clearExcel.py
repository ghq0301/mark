#! python3
# _*_ coding: utf_8  _*_
''' Attention: this will damage all xlsx files' data   2017-2
Add the file name prompt and need comfirm to clear the file.  2017-3-22

''' 
 
import openpyxl
import os
import re
import logging

import getdir

# logging.basicConfig( level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )
logging.basicConfig( level = logging.ERROR, format = ' %(asctime)s - %(levelname)s - %(message)s' )
logging.critical('--------Start of program---------')

for k in range(3):
    input("Attention  %d : this will damage all xlsx files' data. Are you sure." % (k + 1))

# find the file that include '学生名单' in filename
ChineseReg = re.compile(r'学生名单')
excelReg = re.compile(r'.xlsx')

dirname = getdir.getdir()

wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
count = 0
for fileName in os.listdir(dirname):
    if excelReg.search(fileName):
        if ChineseReg.search(fileName) == None:
            print('file %s   will be cleared!' % (fileName))
            input('anykey to continue.')
            wb.save(dirname + '\\' + fileName)
            count += 1
            print('file %s   is clear!' % (fileName))
print('total %d files is clear!' % (count))

logging.critical('-------End--------')
