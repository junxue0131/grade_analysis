import pandas as pd
import os


dirname = os.getcwd()

dirname = dirname.replace('\\', '/')

grades = pd.read_csv(dirname + '/res/final_grade_table.csv')

print('正在生成学生GPA...')

# 计算每个人的GPA和保研GPA
students = grades['sid'].value_counts().index.to_list()

stu_gpa = []
stu_ms_gpa = []
j = 0

# 计算GPA
# TODO:排除课程比较少的人的GPA结果
for i in students:
    print(str(j)+'/'+str(len(students)), end='\r')
    j = j + 1
    credit_sum = grades[grades['sid'] == i]['credit'].sum()
    credit_sum_ms = grades[
        (grades['sid'] == i)
        & ((grades['course_type'] == '公共必修') | (grades['course_type'] == '专业必修'))
        ]['credit'].sum()

    if credit_sum > 15:
        stu_gpa.append(grades[grades['sid'] == i]['weighed_gpa'].sum() / credit_sum)
    else:
        stu_gpa.append(-1)
    if credit_sum_ms > 10:
        stu_ms_gpa.append(grades[
            (grades['sid'] == i)
            & ((grades['course_type'] == '公共必修') | (grades['course_type'] == '专业必修'))
            ]['weighed_gpa'].sum() / credit_sum_ms)
    else:
        stu_ms_gpa.append(-1)


stu_GPA = pd.DataFrame({'sid': students, 'gpa': stu_gpa, 'ms_gpa': stu_ms_gpa})


stu_GPA.to_excel(dirname+'/res/gpa/stu_gpa.xlsx')

print('学生GPA生成完毕')
