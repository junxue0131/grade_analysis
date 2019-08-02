import pandas as pd
import os


dirname = os.getcwd()

dirname = dirname.replace('\\', '/')

grades = pd.read_csv(dirname + '/res/final_grade_table.csv')

print('正在生成学分情况...')

# 整合学分数据
credit_table = grades[['sid', 'year', 'stu_college', 'credit']]
students = grades['sid'].value_counts().index.to_list()
year = []
colleges = []
credit_sum = []

for i in students:
    year.append(credit_table[credit_table['sid'] == i]['year'].iloc[0])
    colleges.append(credit_table[credit_table['sid'] == i]['stu_college'].iloc[0])
    credit_sum.append(credit_table[credit_table['sid'] == i]['credit'].sum())

credit_table = pd.DataFrame({'sid': students, 'year': year, 'college': colleges, 'credit_sum': credit_sum})

# 计算各学院各年级平均学分
# TODO:这里的算法可能有些问题，是不是考虑用典型值替代平均值（因为数据有缺失）
credit_table.groupby(['college', 'year'])['credit_sum'].mean().to_excel(dirname + '/res/credit/credit.xlsx')

# 计算个人所修学分
credit_table.to_excel(dirname + '/res/credit/credit.xlsx')

print('学分情况处理完毕')
