#!/usr/bin/python  
# -*- coding: utf-8 -*-  
# __author__ = 'Ruiyang Ding'

from GPA_calculator import Gpa_Calc, get_sheet
file_name = input('请输入文件名，包含后缀')
sheet = get_sheet(file_name)
ruiyang = Gpa_Calc('ruiyang')
ruiyang.pku(sheet)
ruiyang.zju(sheet)
ruiyang.std(sheet)
ruiyang.stdrev(sheet)
print("北大算法 %f"%ruiyang.get_pkugpa())
print("浙大算法 %f"%ruiyang.get_zjugpa())
print("标准算法 %f"%ruiyang.get_stdgpa())
print("标准改进算法 %f"%ruiyang.get_stdrevgpa())
