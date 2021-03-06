# grade_analysis
武汉大学自强studio数据分析组 学期成绩分析

#### 版本记录
* v0.1.0 脚本初始版本
* v1.0.0 更新脚本为命令行一键操作，略微矫正id_college_map
* v1.0.1 50w的excel表格无法读取，故更改为csv格式

#### TODO
* 修复学号对应学院问题
    * 进一步优化特征学号对应学院Map的精确度问题
    * 根据basic info修复学院改名取消变动问题
* 增加脚本的复用性和可扩展性
    * 改动输入文件输出结果的兼容性 √
    * 突破原有表结构的限制，防止表结构变动产生的不兼容问题
* 增加脚本的数据处理速度
    * 修改iloc式索引，提高索引速度

#### 数据说明
产生的数据结果共包含五部分，分别放置在相应的文件夹内，基本满足了所给的需求
这五部分分别是：

* course
    * hot_course_grade: 包含了这学期上课人数最多的几门课的平均分和挂科率
* credit
    * college_year_credit: 包含了这一学期每个学院每级学生所修的学分
    * stu_credit: 包含了每个学生所修的学分数，降序排列
* gpa
    * college_average_gpa: 包含了这学期各学院的平均gpa
    * stu_gpa: 包含了每个学生这学期的gpa和保研gpa(排除了5学分以下的学生，不具有代表性)
* ka_ji
    * ka_ji: 包含了每个学生的卡绩情况，ka_ji_num指卡绩课程数，no_ka_ji_num指刚好没有被卡绩的课程数
* misc
    * teacher: 包含了所代课的学生最多的前十位老师

#### P.S.
* 尽量用脚本处理一整个学期或一学年的数据
* 学号和学院的对应可能会有一些问题，如果出现反直觉的情况，尽量依靠人为判断
* 所修学分的数据可能因为数据缺失出现反直觉数据，此时尽量依靠人为判断
