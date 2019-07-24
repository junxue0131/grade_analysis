import pandas as pd

path = 'C:/Users/Xue/Desktop/ing/第二学期成绩分析/'

grades = pd.read_csv(path + 'final_grade_table.csv')

print('开始生成学院平均GPA...')

# 计算各院的平均GPA

colleges = grades['stu_college'].value_counts().index.to_list()

gpa_list = []

for i in colleges:
    credit = grades[grades['stu_college'] == i]['credit'].sum()
    gpa_list.append(grades[grades['stu_college'] == i]['weighed_gpa'].sum() / credit)

college_GPA = pd.DataFrame({'college': colleges, 'gpa': gpa_list})

college_GPA.to_csv(path+'/res/college_average_gpa.csv')

print('学院平均GPA生成完毕')
