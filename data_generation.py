import pandas as pd
import os
import sys

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

path_list = []
try:
    path_list.append(dirname + '\\res\\credit')
    path_list.append(dirname + '\\res\\course')
    path_list.append(dirname + '\\res\\gpa')
    path_list.append(dirname + '\\res\\ka_ji')
    path_list.append(dirname + '\\res\\misc')

    for i in path_list:
        os.mkdir(i)
except:
    pass


if __name__ == '__main__':
    try:
        pd.read_excel(dirname + '/res/final_grade_table.xlsx')
    except:
        print('目标文件不存在，请先执行data_reduction确保生成final_grade_table.xlsx文件')
        exit(1)

    os.system('python ' + dirname + '/course/hot_course_mean_grade.py')
    print('\n')
    os.system('python ' + dirname + '/credit/credit.py')
    print('\n')
    os.system('python ' + dirname + '/GPA/college_average_GPA.py')
    print('\n')
    os.system('python ' + dirname + '/GPA/stu_GPA.py')
    print('\n')
    os.system('python ' + dirname + '/ka_ji/ka_ji.py')
    print('\n')
    os.system('python ' + dirname + '/misc/misc.py')

    print('\n所有结果生成完毕')
