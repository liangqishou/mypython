from openpyxl import Workbook
import os, sys
#更改为py文件的当前目录，保存文件的时候可以生成在本目录下。
os.chdir(sys.path[0])

#创建工作簿
wb = Workbook()

#定位到活动的sheet
ws = wb.active
ws['A1'] = 'first'

#创建sheet
ws2 = wb.create_sheet('Sheet2')
ws3 = wb.create_sheet('Sheet3')

#修改sheet名字
ws.title = 'Sheet1_new'

#打印出所有的sheet名字
# 1: 结果为列表
all_sheetname = wb.sheetnames
print(all_sheetname)
# 2: 遍历 loop through
# for i in wb:
#     print(i.title)

# for i in all_sheetname:
#     print(i)

# 复制一个sheet
source_sheet = ws
new_sheet = wb.copy_worksheet(source_sheet)

############### 单元格操作 ###########
c1 = ws['A1']
ws['A2'] = 'second'
ws.cell(row=1, column=2, value='B1')

for i in range(1, 11):
    for j in range(1, 11):
        ws2.cell(row=i, column=j, value=f'{i}-{j}')

# 取多个cell
cell_range = ws2['A1:D2']
cell_range2 = ws2['A1':'D2']
# print(cell_range)
# print(cell_range2)

row_range = ws2[2]
col_range = ws2['B']
# print(row_range)
# print(col_range)


# 取值
print(ws2['A1'].value)
for i in ws2.values:
    for j in i:
        print(j)

a = ws['A1']
print(a.value)
ws['A1'] = 4
print(a.value)
a.value = 5
print(a.value)


#保存文件，如果不存在就新建一个，会覆盖且不提示。
wb.save("test.xlsx")
