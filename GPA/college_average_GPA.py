import pandas as pd

path = 'C:/Users/Xue/Desktop/ing/第二学期成绩分析/'

grades = pd.read_csv(path + 'final_grade_table.csv')

print('开始生成学院平均GPA...')

# 计算各院的平均GPA

colleges = grades['stu_college'].value_counts().index.to_list()
years = grades['year'].value_counts().index.to_list()

gpa_list = []
year = []
college = []

for j in years:
    for i in colleges:
        college.append(i)
        year.append(j)
        credit = grades[(grades['stu_college'] == i) & (grades['year'] == j)]['credit'].sum()
        gpa_list.append(grades[(grades['stu_college'] == i) & (grades['year'] == j)]['weighed_gpa'].sum() / credit)

college_GPA = pd.DataFrame({'college': college, 'gpa': gpa_list, 'year': year})

college_GPA.groupby(['college', 'year'])['gpa'].mean().to_excel(path+'res/gpa/college_average_gpa.xlsx')


print('学院平均GPA生成完毕')
