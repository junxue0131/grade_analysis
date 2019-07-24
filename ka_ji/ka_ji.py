import pandas as pd

path = 'C:/Users/Xue/Desktop/ing/第二学期成绩分析/'

grades = pd.read_csv(path + 'final_grade_table.csv')


# 计算卡绩
def get_ka_ji(row):
    if row.grade == 89:
        return 1
    elif row.grade == 84:
        return 1
    elif row.grade == 81:
        return 1
    elif row.grade == 77:
        return 1
    elif row.grade == 74:
        return 1
    elif row.grade == 71:
        return 1
    elif row.grade == 67:
        return 1
    elif row.grade == 63:
        return 1
    elif row.grade == 59:
        return 1
    else:
        return 0


# 计算未被卡绩
def get_no_ka_ji(row):
    if row.grade == 90:
        return 1
    elif row.grade == 85:
        return 1
    elif row.grade == 82:
        return 1
    elif row.grade == 78:
        return 1
    elif row.grade == 75:
        return 1
    elif row.grade == 72:
        return 1
    elif row.grade == 68:
        return 1
    elif row.grade == 64:
        return 1
    elif row.grade == 60:
        return 1
    else:
        return 0


print('正在生成学生卡绩情况...')

# 计算每个人的卡绩情况
students = grades['sid'].value_counts().index.to_list()

ka_ji_num = []
no_ka_ji_num = []
j = 0

for i in students:
    print(str(j)+'/'+str(len(students)))
    j = j + 1
    ka_ji_num.append(grades[grades['sid'] == i].apply(get_ka_ji, axis=1).sum())
    no_ka_ji_num.append(grades[grades['sid'] == i].apply(get_no_ka_ji, axis=1).sum())

stu_ka_ji = pd.DataFrame({'stu': students, 'ka_ji_num': ka_ji_num, 'no_ka_ji_num': no_ka_ji_num})

stu_ka_ji.to_excel(path+'/res/ka_ji.xlsx')

print('卡绩情况生成完毕')
