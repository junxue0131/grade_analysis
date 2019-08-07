# TODO:改成OOP式

import pandas as pd
import json

import os
import sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

os.mkdir(dirname + '\\res')

if __name__ == '__main__':
    course_path = input('请输入课程信息文件路径：').replace('\\', '/')
    grade_path = input('请输入成绩信息文件路径：').replace('\\', '/')

    print(course_path)
    print(grade_path)

    grades = pd.read_csv(grade_path)
    courses = pd.read_csv(course_path)

    print('读取文件完成')


    # remove empty grade
    def remove_empty_grade(row):
        if row['grade'] == -1:
            return
        else:
            return row['grade']


    grades['grade'] = grades.apply(remove_empty_grade, axis=1)
    grades = grades.dropna()

    print('空成绩移除完成')


    # add year col
    def get_year(row):
        return str(row['sid'])[0:4]


    grades['year'] = grades.apply(get_year, axis=1)

    print('年级获取成功')

    # match course_id
    print('正在匹配每门成绩的课程信息...')
    j = 0


    # 采用iloc非常慢,学号可能出错
    def match_course_info(row):
        global j
        j = j + 1
        print(str(j) + '/' + str(len(grades)), end='\r')
        try:
            return courses[courses['id'] == int(row.course_id)].iloc[0][[
                'name', 'course_type', 'credit', 'instructor', 'college', 'major'
            ]]
        except:
            return 'nan'


    grades[[
        'name', 'course_type', 'credit', 'instructor', 'college', 'major'
    ]] = grades.apply(match_course_info, axis=1)[[
        'name', 'course_type', 'credit', 'instructor', 'college', 'major'
    ]]

    print('匹配每门成绩的课程信息完成')


    # get GPA
    def one_class_GPA(row):
        if row['grade'] < 60:
            return 0
        if row['grade'] < 64:
            return 1
        if row['grade'] < 68:
            return 1.5
        if row['grade'] < 72:
            return 2
        if row['grade'] < 75:
            return 2.3
        if row['grade'] < 78:
            return 2.7
        if row['grade'] < 82:
            return 3
        if row['grade'] < 85:
            return 3.3
        if row['grade'] < 90:
            return 3.7
        else:
            return 4


    grades['GPA'] = grades.apply(one_class_GPA, axis=1)

    print('每门课程的GPA计算完成')


    # 计算加权GPA
    def get_weighed_gpa(row):
        try:
            return row['GPA'] * row['credit']
        except:
            return 'nan'


    grades['weighed_gpa'] = grades.apply(get_weighed_gpa, axis=1)

    print('每门课程的加权GPA计算完成')

    # 匹配学生的学院
    print('正在匹配学生的学院...')


    # 增加短学号字段，以便划分学院
    def get_short_id(row):
        return str(row.sid)[0:9]


    grades['short_id'] = grades.apply(get_short_id, axis=1)

    # 通过短学号和学院——学号map来对应出学院
    f = open('id_college_map.json', 'r')
    map = f.read()
    f.close()

    map = json.loads(map)


    def get_college(row):
        for k in map:
            if row.short_id in map[k]:
                return k


    grades['stu_college'] = grades.apply(get_college, axis=1)

    print('匹配学生的学院完成')


    # make course_type num to 4 kinds
    def course_type_reduct(row):
        if row.course_type == '专业教育必修':
            return '专业必修'
        elif row.course_type == '公共基础必修':
            return '公共必修'
        elif row.course_type == '通识教育选修' or row.course_type == '公共基础选修':
            return '公共选修'
        elif row.course_type == '专业教育选修':
            return '专业选修'
        else:
            return row.course_type


    grades['course_type'] = grades.apply(course_type_reduct, axis=1)

    print('清除冗余课程分类完成')

    # delete useless cols
    del grades['id']
    del grades['created_at']
    del grades['updated_at']
    del grades['semester']
    del grades['short_id']

    print('删除冗余列完成')

    grades.columns = ['sid', 'year', 'grade', 'learning_type', 'course_id', 'name',
                      'course_type', 'credit', 'instructor', 'course_college', 'course_major', 'GPA',
                      'weighed_gpa', 'stu_college']

    print('列名重命名完成')

    # generate final grade_table
    grades.to_csv(dirname.replace('\\', '/') + '/res/final_grade_table.csv')

    print('文件保存成功:' + dirname.replace('\\', '/') + '/res/final_grade_table.csv')
