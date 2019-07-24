import pandas as pd

path = 'C:/Users/Xue/Desktop/ing/第二学期成绩分析/'

grades = pd.read_csv(path + 'final_grade_table.csv')

print('正在生成课程给分情况')


def get_fail_num(row):
    if row.grade < 60:
        return 1
    else:
        return 0


# 分析热门课程给分情况
hot_course = grades['name'].value_counts()
hot_course = hot_course[hot_course > 20].index.to_list()
course_mean_grade = []
fail_rate = []
course_type = []

for i in hot_course:
    course_type.append(grades[grades['name'] == i]['course_type'].iloc[0])
    fail_rate.append(
        grades[grades['name'] == i].apply(get_fail_num, axis=1).sum() / grades[grades['name'] == i]['grade'].count())
    course_mean_grade.append(grades[grades['name'] == i]['grade'].mean())

hot_course_mean_grade = pd.DataFrame(
    {'name': hot_course, 'course_type': course_type, 'grade': course_mean_grade, 'fail_rate': fail_rate})

hot_course_mean_grade.to_excel(path + '/res/hot_course_grade.xlsx')

print('课程给分情况生成完毕')
