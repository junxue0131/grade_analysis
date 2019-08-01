gpa1 = pd.read_excel('C:/Users/Xue/Desktop/college_average_gpa1')
gpa2 = pd.read_excel('C:/Users/Xue/Desktop/college_average_gpa2')

# 删除gpa1和gpa2的重复列

a = gpa1.set_index("sid").join(gpa2.set_index("sid"))

def delete(row):
    if row.gpa1 == -1 or row.gpa2 == -1:
        return None
    else:
        return row

a = a.apply(delete, axis=1)

a['gpa_change'] = a['gpa2'] - a['gpa1']