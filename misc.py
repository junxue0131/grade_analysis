import pandas as pd

path = 'C:/Users/Xue/Desktop/ing/第二学期成绩分析/'

grades = pd.read_csv(path + 'final_grade_table.csv')


# 统计上课最多的老师
teachers = grades.drop_duplicates('name')['instructor'].value_counts()[:10]

teacher_name = teachers.index.to_list()

teacher_num = teachers.to_list()

teachers = pd.DataFrame([teacher_name, teacher_num]).T

teachers.columns = [['teacher_name', 'num']]


def match_college(row):
    return grades[grades['instructor'] == str(row[0])]['course_college'].dropna().iloc[0]


teachers['college'] = teachers.apply(match_college, axis=1)

teachers.to_excel(path+'/res/misc/teacher.xlsx')