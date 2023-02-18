import openpyxl
import os, sys
os.chdir(sys.path[0])
# 打开Excel文件
workbook = openpyxl.load_workbook('test.xlsx')

# 循环遍历每个工作表
for sheet_name in workbook.sheetnames:
    sheet = workbook[sheet_name]

    # 循环遍历每列
    for column in sheet.columns:
        # 获取列的字母
        column_letter = column[0].column_letter

        # 获取列中最宽的单元格的宽度
        max_length = 0
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass

        # 根据最宽的单元格的宽度调整列的宽度
        adjusted_width = (max_length + 2)
        sheet.column_dimensions[column_letter].width = adjusted_width

# 保存修改后的Excel文件
workbook.save('test.xlsx')
