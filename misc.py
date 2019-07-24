import pandas as pd

path = 'C:/Users/Xue/Desktop/ing/第二学期成绩分析/'

grades = pd.read_csv(path + 'final_grade_table.csv')


# 统计上课最多的老师
grades.drop_duplicates('name')['instructor'].value_counts()[:10].to_excel(path+'/res/teacher.xlsx')