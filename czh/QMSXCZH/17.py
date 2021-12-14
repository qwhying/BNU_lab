import numpy as np
import pandas as pd
import xlrd

#2
io = r'D:\程序设计\BNU_lab\BNU_lab\czh\期末实训数据-我好想要买点什么.xlsx'
data = pd.read_excel(io, sheet_name=0)
# print(data)

#3
# czh=data[(data["姓名"] =="陈之豪") & (data["学号"] =="20012760")]
# print(czh)
print(data["姓名"])